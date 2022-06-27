def count_find_num(primesL, limit):
    first_mult = 1
    for value in primesL:
        first_mult *= value
    if first_mult > limit:
        return []
    result = [first_mult]

    for i in primesL:
        for value in result:
            number = value * i
            if (number <= limit) and (number not in result):
                result.append(number)
                number *= i

    return [len(result), max(result)]



primesL = [2, 3]
limit = 200
assert count_find_num(primesL, limit) == [13, 192]

primesL = [2, 5]
limit = 200
assert count_find_num(primesL, limit) == [8, 200]

primesL = [2, 3, 5]
limit = 500
assert count_find_num(primesL, limit) == [12, 480]

primesL = [2, 3, 5]
limit = 1000
assert count_find_num(primesL, limit) == [19, 960]

primesL = [2, 3, 47]
limit = 200
assert count_find_num(primesL, limit) == []
