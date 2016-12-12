from math import ceil, sqrt

if __name__ == "__main__":
    bound = 1000
    ab_bnd = int(ceil(bound/2)+1)
    for a in range(1,ab_bnd):
        for b in range(1,ab_bnd):
            csq = a**2 + b**2
            c = sqrt(csq)
            if a + b + c == 1000:
                print(a, b, c, a*b*c)
