import itertools


def bananas(s):
    result = set()
    for combination in itertools.combinations(range(len(s)), len(s) - len('banana')):
        letters = list(s)
        for i in combination:
            letters[i] = '-'
        str_to_check = ''.join(letters)
        if str_to_check.replace('-', '') == 'banana':
            result.add(str_to_check)
    return result


assert bananas("banann") == set()
assert bananas("banana") == {"banana"}
assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                     "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                     "-ban--ana", "b-anana--"}
assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}
