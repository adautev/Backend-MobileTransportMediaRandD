#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import OpenSSL
st_cert = open('pki/provisioning/certs/server_side.key').read()
certificate = OpenSSL.crypto.load_privatekey(OpenSSL.crypto.FILETYPE_PEM, st_cert, passphrase="adiadi")
private_key = ""