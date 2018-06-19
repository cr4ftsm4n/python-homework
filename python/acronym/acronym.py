import re
def abbreviate(words):
    str = ""
    for i in re.split(r'[ -]',words) :
        str += i[0]
        
    return str.upper()
