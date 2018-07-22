def numeral(number):
    num_list=[1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]  
    str_list=["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]  
    res=''  
    for i in range(len(num_list)):  
        while number>=num_list[i]:  
            number-=num_list[i]  
            res+=str_list[i]  
    return res
