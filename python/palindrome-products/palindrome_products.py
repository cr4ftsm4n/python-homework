def largest_palindrome(max_factor, min_factor):
    value = 0
    factors = []
    list_factor = list(range(min_factor, max_factor + 1))
    
    for i in list_factor[::-1]:
        for j in list_factor[::-1]:   
            a = str(i*j)[::-1]
            if a == str(i*j):
                if value < i*j:
                    value = i*j  
    if value == 0:
        raise ValueError("error")
        
    for i in list_factor:
        if value%i == 0 and value/i in list_factor:
            if i <= value/i:
                factors.append((i, int(value/i)))
            else:
                break
                
    return (value, factors)        
                

def smallest_palindrome(max_factor, min_factor):
    value = 0
    factors = []
    list_factor = list(range(min_factor, max_factor + 1))
    for i in list_factor:
        for j in list_factor:
            a = str(i*j)[::-1]
            if a == str(i*j):
                if value > i*j:
                    value = i*j
            
    if value == 0:
        raise ValueError("error")
        
    for i in list_factor:
        if value%i == 0 and value/i in list_factor:
            if i <= value/i:
                factors.append((i, int(value/i)))
            else:
                break
                
    return (value, factors)     
