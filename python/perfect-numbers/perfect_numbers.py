def classify(number):
    if number < 1:
        raise ValueError("error")
    sum = 0
    for divisor in range(1, number):
        if not number % divisor:
            sum += divisor
    if sum == number:
        return "perfect"
    elif sum > number:
        return "abundant"
    else:
        return "deficient"
