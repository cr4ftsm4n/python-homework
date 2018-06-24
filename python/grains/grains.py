def on_square(integer_number):
    if integer_number < 1 or integer_number > 64:
        raise ValueError("error")
    else:
        return 2**(integer_number-1)


def total_after(integer_number):
    total = 0
    if integer_number < 1 or integer_number > 64:
        raise ValueError("error")
    else:
        for i in range(integer_number):
            total += 2**i
    return total
