import random

def find_primes(n=100):
    primes = []
    for c in range(2, n + 1):
        is_prime = True
        for d in range(2, c):
            if c % d == 0:
                is_prime = False
                break
        if is_prime:
            print(f"{c} is prime")
            primes.append(c)
    return primes

def trial_composite(a):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n-1:
            return False
    return True  

def miller_rabin(n, k=1):
    # step 1: represent n=2^s * t + 1
    print("Probability of False positive=", 4 ** (-k))
    if n % 2 == 0:
        return False
    s = 0
    d = n - 1
    while d % 2 == 0:
        d /= 2
        s += 1
    d = int(d)
    for trial in range(k):
        a = random.randrange(2, n)
        
        if pow(a, d, n) == 1:
            continue
        next = False
        for i in range(s):
            if pow(a, 2 ** i * d, n) == n - 1:
                next = True
                break
        if next:
            continue
        else:
            return False
    return True

if __name__ == '__main__':
    v = [miller_rabin(_) for _ in find_primes()[1:]]
    print("sum(v)=", sum(v))
    print("True probability = ", sum(v) / len(v))