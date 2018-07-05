def char_value(c):
    c = c.upper()
    if c in "AEIOULNRST":
        return 1
    elif c in "DG":
        return 2
    elif c in "BCMP":
        return 3
    elif c in "FHVWY":
        return 4
    elif c in "K":
        return 5
    elif c in "JX":
        return 8
    elif c in "QZ":
        return 10
    else:
        return 0


def score(word):
    total = 0
    for c in word:
        total += char_value(c)
    return total
