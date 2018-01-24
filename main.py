#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import string
from random import choice, randint

import jsonpickle as jsonpickle
from flask import Flask, Response
# lame but I don't need more of a migration strategy
from flask_migrate import Migrate, Manager, MigrateCommand
from flask_sqlalchemy import SQLAlchemy

from dal.config import Config

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = Config.SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)

from dal.available_products import AvailableProducts
from dal.used_products import UsedProducts

migrate = Migrate(app, db)


@app.route('/token/<string:uuid>')
def token(uuid):
    min_char = 100
    max_char = 120
    all_characters = string.ascii_letters + string.punctuation + string.digits
    token = "".join(choice(all_characters) for x in range(randint(min_char, max_char)))
    return Response(jsonpickle.encode({
        "token": token,
        "uuid": uuid
    }, unpicklable=False),
        mimetype='application/json; charset=utf-8')
