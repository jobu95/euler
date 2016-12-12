# a prime number generator. it yields all prime numbers by a trivial prime
# factorization test.
#
# interesting factoid about this generator: it runs in o(pi(n)) time and space,
# where pi(n) is the so-called 'prime counting function'!
def primes():
    n = 2
    primes = []
    # whenever a number is appended to primes, it is prime. so we emit it
    primes.append(n)
    yield 2
    n = n + 1
    while True:
        is_prime = True
        for prime in primes:
            if n % prime == 0:
                is_prime = False
        if is_prime:
            primes.append(n)
            yield n
        n = n + 2

# return prime factors of x
def factor(x):
    # for now, don't allow negative numbers
    if (x <= 1):
        return []
    pgen = primes()
    factors = []
    while x > 1:
        p = pgen.next()
        while x % p == 0:
            factors.append(p)
            x = x / p
    return factors

if __name__ == "__main__":
    factors = factor(600851475143)
    for f in factors:
        print(f)
    print("largest factor: " + str(factors[-1]))
