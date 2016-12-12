# solve problem by use of a generator. this generator, firstnfibs, returns all
# even fibonacci numbers underneath a cap n. use this to get the answer:
#   sum(firstnfibs(4000000))
def firstnfibs(n):
    s1 = 1
    s2 = 2
    while s1 < n:
        if s1 % 2 == 0:
            yield s1
        # make s2 = s1 + s2 and s1 = old s2 - i.e., compute next fib num
        s = s2
        s2 = s1 + s2
        s1 = s

fibsum = sum(firstnfibs(100))
print(fibsum)
print(firstnfibs(100))
