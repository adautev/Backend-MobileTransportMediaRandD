#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import string
from random import choice, randint
import jsonpickle as jsonpickle
from flask import Flask, Response

app = Flask(__name__)
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