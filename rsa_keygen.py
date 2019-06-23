from rsa_main import *
import pickle
import sys

if __name__ == "__main__":
    print("Generating p and q:")
    p, q = p_q_generation()
    print("Generating keypair")
    keys = generate_keypair(p, q)
    with open("keypair.pem" if len(sys.argv) == 1 else sys.argv[1], "wb+") as f:
      pickle.dump(keys, f)
    print("Done")