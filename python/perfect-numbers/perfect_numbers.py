def classify(number):
    if number in [0, -1]:
        raise ValueError("bad value")
    total = []
    for i in range(1, number):
        if number % i == 0:
            total.append(i)
    s = sum(total)
    if s == number:
        return "perfect"
    elif s < number:
        return "deficient"
    else:
        return "abundant"
