def translate(text):
    list = text.lower().split(" ")
    for i in range(len(list)):
        if list[i][:1] in "aeiou" or list[i][:2] == "xr" or list[i][:2] == "yt":  
            list[i] = list[i]+"ay"
        else:
            if list[i].find("qu") != -1:
                list[i] = list[i][list[i].find("qu")+2:]+list[i][:list[i].find("qu"):] + "quay"
            else:
                num =getIndex(list[i])
                list[i] = list[i][num:]+list[i][0:num]+"ay"
                
    str_pig_latin = ""
    for i in range(len(list)):
        if i > 0:
            str_pig_latin += " "
        str_pig_latin += list[i]
        
    return str_pig_latin
    
def getIndex(s):
    for i in range(len(s)):
        if((s[i] in "aeiou") or (i!=0 and s[i] =="y")):
            return i
    return len(s)
