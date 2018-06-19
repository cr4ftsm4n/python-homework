import locale

NUMBER_CONSTANT = {0:"zero", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven",  
                8:"eight", 9:"nine", 10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen",  
                14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen" }
IN_HUNDRED_CONSTANT = {2:"twenty", 3:"thirty", 4:"forty", 5:"fifty", 6:"sixty", 7:"seventy", 8:"eighty", 9:"ninety"}  
BASE_CONSTANT = {0:" ", 1:"hundred", 2:"thousand", 3:"million", 4:"billion"}

def say(number):
    number = int(number)
    str_number = u""
    str_number += str(locale.format("%d", number, grouping=True))
    if str_number.isnumeric() and len(str_number) < 13 and number >= 0:  
        if str_number[0] == '0' and len(str_number) > 1:  
            return say(int(number[1:]))
        if int(number) < 20:  
            return NUMBER_CONSTANT[int(number)] 
        elif int(number) < 100:  
            if str_number[1] == '0':  
                return IN_HUNDRED_CONSTANT[int(str(number)[0])]
            else:  
                return IN_HUNDRED_CONSTANT[int(str(number)[0])] + "-" + NUMBER_CONSTANT[int(str(number)[1])]
        else:   
            strNumber = format(number,',')
            numberArray = strNumber.split(",")  
            stringResult = ""  
            groupCount = len(numberArray) + 1 
            last = ""
            for groupNumber in numberArray:
                if groupCount > 1 and groupNumber[0:] != "000":
                    stringResult += str(getUnderThreeNumberString(str(groupNumber),last)) + " "                 
                    last = groupNumber[len(groupNumber)-1:]
                else:
                    groupCount -= 1 
                    last = groupNumber[len(groupNumber)-1:]
                    continue
                groupCount -= 1 
                if groupCount > 1:  
                    stringResult += BASE_CONSTANT[groupCount] + " " 
                
            endPoint = len(stringResult) - len(" hundred,")  
            return stringResult.strip()
                  
    else:  
        raise ValueError("error")
        
def getUnderThreeNumberString(number, last):   
    str_number = u""
    str_number += str(number).lstrip("0")
    str_temp = ""
    if str_number.isnumeric() and len(number) < 4:  
        if len(number) < 3:  
            str_temp = say(int(number))
        elif len(number) == 3 and number[0:] == "000":  
            str_temp = " "
        elif len(number) == 3 and len(number.lstrip("0")) < 3:
            str_temp = say(int(number))
        elif len(number) == 3 and number[1:] == "00":  
            str_temp = NUMBER_CONSTANT[int(number[0])] + " " + BASE_CONSTANT[1]  
        else:      
            str_temp = NUMBER_CONSTANT[int(number[0])] + " " + BASE_CONSTANT[1] + " and " + say(int(number[1:]))
        if last == "0":
            str_temp = "and " + str_temp
        return str_temp      
    else:  
        raise ValueError("error")
