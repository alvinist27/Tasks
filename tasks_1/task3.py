def zeros(n):
    counter = 0
    while n > 0:
        n //= 5
        counter += n
    return counter


assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(30) == 7
