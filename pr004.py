def palindromes():
    max_pal = 0
    i = 101
    while i <= 999:
        j = 101
        while j <= 999:
            product = i*j
            pstr = str(product)
            if pstr == pstr[::-1] and product > max_pal: # reverse string
                max_pal = product
            j = j + 2
        i = i + 2
    return max_pal

if __name__ == "__main__":
    print(palindromes())
