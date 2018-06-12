def reverse(input=''):
    res=""
    for i in range(len(input)):
        res=res+input[len(input)-1-i]
    return res
