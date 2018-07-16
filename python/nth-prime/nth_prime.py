def nth_prime(positive_number):
    if positive_number < 1:
        raise ValueError("error")
    count = 0
    prime = 2
    while count != positive_number:
        if prime == 2:
            count += 1
            if count == positive_number:
                break
            else:
                prime += 1
                continue
        for i in range(1,prime):
            if prime%i == 0 and i != 1:
                prime += 2
                continue
            else:
                if i == prime-1:
                    count += 1
                    if count == positive_number:
                        break
                    else:
                        prime += 2
    return prime
        
