from pr003 import primes

if __name__ == "__main__":
    pgen = primes()
    p = 0
    for _ in range(10001):
        p = pgen.next()
    print(p)
