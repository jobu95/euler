# compute the sum of squares of the first n natural numbers
def sqsum(n):
    if n < 1:
        return 0
    def iter(cur, acc):
        if cur == 0:
            return acc
        else:
            return iter(cur - 1, acc + cur**2)
    return iter(n, 0)

# compute the square of the sum of the first n natural numbers
def sumsq(n):
    if n < 1:
        return 0
    def iter(cur, acc):
        if cur == 0:
            return acc
        else:
            return iter(cur - 1, acc + cur)
    return iter(n, 0)**2

if __name__ == "__main__":
    print(sumsq(100) - sqsum(100))
