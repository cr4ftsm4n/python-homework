plain="abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba"

def encode(plain_text):
    cipher = ""
    count = 0
    for x in plain_text.lower():
        if x.isalpha():
            cipher += plain[ord(x)-ord("a")+ 26]
            count += 1
        elif x.isalnum():
            cipher += x
            count += 1
        else:
            continue
        
        if count%5 == 0 and count != 0:
            cipher += " "
            
    return cipher.rstrip()
            
        
def decode(ciphered_text):
    strplain = ""
    
    for x in ciphered_text:
        if x.isalpha():
            strplain += plain[ord(x)-ord("a")+ 26]
        elif x.isalnum():
            strplain += x
        else:
            continue
            
    return strplain
            
