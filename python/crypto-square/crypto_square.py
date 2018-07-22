import math
def encode(plain_text):
    str_plain_text = ""
    for i in plain_text:
        if i.isalnum() == True:
            str_plain_text += i
            
    str_plain_text = str_plain_text.lower()
    if str_plain_text == "":
        return ""
    
    row = 0
    cloum = 0
    r = 0
    for c in range(1,len(str_plain_text)+1):
        r = int(math.ceil(len(str_plain_text)/float(c)))
        if r <= c and c - r <= 1:
            row = r
            cloum = c
            break

    str_output = ""
    i = 0
    count = 0
    for i in range(cloum):
        a = i
        count = 0
        while a < len(str_plain_text):
            if a == i and i != 0:
                str_output += " "
            str_output += str_plain_text[a]
            count += 1
            a += cloum
            if a >= len(str_plain_text) and count < row:
                for s in range(row-count):
                    str_output += " "
    return str_output
