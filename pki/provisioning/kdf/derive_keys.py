#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

# I am almost well aware I am using two libs that almost do the same. :D
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Protocol.KDF import PBKDF2
from Crypto.PublicKey import RSA

master_key = b'Start wearing purple!'
salt = os.urandom(128)
#
# parser = argparse.ArgumentParser(description='PKI encryption certificate passphrase')
# parser.add_argument('passphrase', metavar='P', type=str, nargs='+',
#                    help='PKI encryption certificate passphrase')
#
# args = parser.parse_args()

cert = open('pki/provisioning/certs/encryption-certificate.key').read()
# rsa = RSA.import_key(cert, args.passphrase[0])
rsa = RSA.import_key(cert)
kfg = PBKDF2(password=master_key, salt=salt)
session_key = os.urandom(16)

# Encrypt the session key with the public RSA key
cipher_rsa = PKCS1_OAEP.new(rsa)
file_out = open("encrypted_key.bin", "wb")
# Encrypt the session key with the public RSA key
file_out.write(cipher_rsa.encrypt(session_key))
# Encrypt the data with the AES session key
cipher_aes = AES.new(session_key, AES.MODE_EAX)
ciphertext, tag = cipher_aes.encrypt_and_digest(kfg)
[file_out.write(x) for x in (cipher_aes.nonce, tag, ciphertext)]
