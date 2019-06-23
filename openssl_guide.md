# OpenSSL RSA implementation usage guide

## Key generation

`openssl genrsa -out key.pem <numbits>`

This generates a public-private key pair

* `numbits` must be greater than 64 bits. Default to 2048
* key generation is a random process

## Key encryption

`openssl genrsa -out <name> -<cipher> <numbits>`


### Output format
* Every `.` represents a number which has passed an initial sieve test
* Every `+` means that such number has passed a single round of the Miller-Rabin primality test
* `\n` indicates that number has passed all the prime tests
* There are three output formats "SSLeay", "PKCS#1" and "PKCS#8"

## Encrypt message

`openssl pkeyutl -encrypt -in <plaintext> -inkey <key.pem>`

## Decrypt message

`openssl pkeyutl -decrypt -in <enctext> -inkey <key.pem>`
