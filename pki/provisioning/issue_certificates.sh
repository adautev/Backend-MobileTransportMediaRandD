#!/usr/bin/env bash
#request the server side certificate
openssl req -new \
    -config etc/server-side.conf \
    -out certs/server-side.csr \
    -keyout certs/server_side.key
#issue the server side certificate
openssl ca \
    -config etc/signing-ca.conf \
    -in certs/server-side.csr \
    -out certs/server-side.crt
#request the validator certificate
openssl req -new \
    -config etc/validator.conf \
    -out certs/validator.csr \
    -keyout certs/validator.key
#issue the validator certificate
openssl ca \
    -config etc/signing-ca.conf \
    -in certs/validator.csr \
    -out certs/validator.crt