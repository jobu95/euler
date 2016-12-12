# greatest common divisor of a and b. compute via euclid's algorithm
def gcd(a, b):
    if (b == 0):
        return a
    return gcd(b, a % b)

# least common multiple of a and b
def lcm(a, b):
   return  a * b / gcd(a,b)

if __name__ == "__main__":
    fold = 1
    for i in range(1,20):
        fold = lcm(i, fold)
    print(fold)
