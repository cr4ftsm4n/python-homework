def is_armstrong(number):
    strnum = str(number)
    sum = 0
    for i in strnum:
        sum += int(i)**len(strnum)
        
    if sum == number:
        return True
    else:
        return False
