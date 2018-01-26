#!/usr/bin/env bash
#request the server side certificate
openssl req -new \
    -config etc/encryption-certificate.conf \
    -out certs/encryption-certificate.csr \
    -keyout certs/encryption-certificate.key
#issue the server side certificate (too lazy to change .conf, as I will not be expanding public properties for now)
openssl ca \
    -config etc/encryption-certificate.conf \
    -in certs/encryption-certificate.csr \
    -out certs/encryption-certificate.crt
#request the validator certificate
