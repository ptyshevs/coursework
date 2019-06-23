from rsa_main import *
import pickle
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
      print("usage: ./rsa_encrypt.py <keypair.pem>")
    public, private = pickle.load(open(sys.argv[1], 'rb'))
    cipher = encrypt(public, input("Enter text:"))
    print("ciphertext:" + ''.join([chr(_) for _ in cipher]))