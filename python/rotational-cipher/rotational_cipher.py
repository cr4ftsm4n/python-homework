def rotate(text, key):
    strtemp = ""
    
    for i in text:
        if i.isalpha():
            keytemp = ord(i) + key
            if ord(i) >= 97 and ord(i) <= 122 and keytemp > 122:
                strtemp += chr(keytemp-122+96)
            elif ord(i) >= 65 and ord(i) <= 90 and keytemp > 90:
                strtemp += chr(keytemp-90+64)
            else:
                strtemp += chr(keytemp)
        else:
            strtemp += i
            
    return strtemp

