#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import base64
import string
from random import choice, randint

import datetime
import jsonpickle as jsonpickle
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.PublicKey import RSA
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
            #prepare pki
            # assumably in a safe place
            cert = open('pki/provisioning/certs/encryption-certificate.key').read()
            rsa = RSA.import_key(cert)
            file_in = open("encrypted_key.bin", "rb")
            enc_session_key, nonce, tag, ciphertext = \
                [file_in.read(x) for x in (rsa.size_in_bytes(), 16, 16, -1)]

            # Decrypt the session key with the public RSA key
            cipher_rsa = PKCS1_OAEP.new(rsa)
            session_key = cipher_rsa.decrypt(enc_session_key)

            # Decrypt the data with the AES session key
            cipher_aes = AES.new(session_key, AES.MODE_EAX)
            encryption_key = cipher_aes.decrypt(ciphertext)
            #lame time prediction. :D Add a few seconds lag.
            valid_from = datetime.datetime.now() + datetime.timedelta(seconds=5)
            valid_to = valid_from + datetime.timedelta(seconds=60)
            issued_token = IssuedToken(product_id=product_id, consumer_id=consumer_id, valid_from = valid_from, valid_to = valid_to)
            db.session.add(issued_token)
            db.session.commit()
            cipher_aes = AES.new(encryption_key, AES.MODE_EAX)
            ciphertext, received_tag= cipher_aes.encrypt_and_digest(bytes(jsonpickle.encode({
                "product_id":product_id,
                "consumer_id":consumer_id,
                "valid_from":valid_from,
                "valid_to":valid_to
            }).encode('utf-8')))
            nonce = cipher_aes.nonce
            # cipher_aes = AES.new(encryption_key, AES.MODE_EAX, nonce)
            # decoded_text = cipher_aes.decrypt_and_verify(ciphertext, received_tag)
            return Response(jsonpickle.encode({
                "transport_document": base64.b64encode(ciphertext).decode('ascii'),
                "tag": base64.b64encode(received_tag).decode('ascii'),
                "valid_from": valid_from,
                "valid_to": valid_to,
                "nonce": base64.b64encode(nonce).decode('ascii')

            }, unpicklable=False),
                mimetype='application/json; charset=utf-8')
    except:
        db.session.rollback()
        raise
    finally:
        db.session.close()