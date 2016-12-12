from pr003 import primes

if __name__ == "__main__":
    cap = 2000000
    pgen = primes()
    psum = 0
    p = pgen.next()
    while p < cap:
        psum = psum + p
        p = pgen.next()
    print(psum)
