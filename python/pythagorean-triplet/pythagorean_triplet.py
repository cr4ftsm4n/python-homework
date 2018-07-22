import math
def IsPrime(m, n):
    for i in range(2,n+1):
        if m%i == 0 and n%i == 0:
            return False
    return True

def primitive_triplets(number_in_triplet):
    lst = []
    for i in range(1, number_in_triplet):
        for j in range(i, number_in_triplet):
            if 2*i*j == number_in_triplet:
                if (j**2-i**2)**2 + number_in_triplet**2 == (j**2+i**2)**2:
                    if i>0 and j>0 and IsPrime(j, i) == True:
                        lst_temp = [(j**2-i**2),number_in_triplet,(j**2+i**2)]
                        lst_temp.sort()
                        lst.append((lst_temp[0],lst_temp[1],lst_temp[2]))
    
    if len(lst) == 0:
        raise ValueError("error")
    c = set(lst)
    return c


def triplets_in_range(range_start, range_end):
    lst = []
    for i in range(range_start,range_end + 1):
        for j in range(i,range_end + 1):
            for k in range(j,range_end + 1):
                if i**2 + j**2 == k**2:
                    lst.append((i,j,k))
    
    c = set(lst)
    return c


def is_triplet(triplet):
    lst = list(triplet)
    lst.sort()
    
    if lst[0]**2 + lst[1]**2 == lst[2]**2:
        return True
    else:
        return False
        
