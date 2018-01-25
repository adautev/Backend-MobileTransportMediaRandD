#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import string
from random import choice, randint

import datetime
import jsonpickle as jsonpickle
from flask import Flask, Response
# lame but I don't need more of a migration strategy
from flask_migrate import Migrate, Manager, MigrateCommand
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from dal.config import Config


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = Config.SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)

from dal.available_product import AvailableProduct
from dal.used_product import UsedProduct
from dal.issued_token import IssuedToken

migrate = Migrate(app, db)
engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)

@app.route('/token/<string:product_id>/<string:consumer_id>')
def token(product_id, consumer_id):
    #Check whether there is a product available:
    try:
        product = db.session.query(AvailableProduct).filter_by(product_id = product_id, consumer_id = consumer_id).one_or_none()
        if product is None:
            return Response(status=401)
        else:
            #lame time prediction. :D Add a few seconds lag.
            valid_from = datetime.datetime.now() + datetime.timedelta(seconds=5)
            valid_to = valid_from + datetime.timedelta(seconds=60)
            issued_token = IssuedToken(product_id=product_id, consumer_id=consumer_id, valid_from = valid_from, valid_to = valid_to)
            db.session.add(issued_token)
            db.session.delete(product)
            db.session.commit()
            return Response(jsonpickle.encode(issued_token, unpicklable=False),
                mimetype='application/json; charset=utf-8')
    except:
        db.session.rollback()
        raise
    finally:
        db.session.close()