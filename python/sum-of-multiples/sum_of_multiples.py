def sum_of_multiples(limit, multiples):
    count = 0
    for i in range(limit):
        for x in multiples:
            if i%x == 0:
                count += i
                break
    return count
