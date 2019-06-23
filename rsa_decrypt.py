from rsa_main import *
import pickle
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
      print("usage: ./rsa_encrypt.py <keypair.pem>")
    public, private = pickle.load(open(sys.argv[1], 'rb'))
    plaintext = decrypt(private, input("Enter cipher:"))
    print("plaintext:", plaintext)