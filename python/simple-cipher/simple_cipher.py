class Cipher(object):
    plain="abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    key = ""
    count = []
    def __init__(self, key=None):
        self.key = ""
        self.count = []
        if key == None:
            self.key = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        elif key.isalpha() == False or key.islower() == False:
            raise ValueError("Cipher('" + key +"')")
        else:    
            self.key = key
        for i in self.key:
            self.count.append(ord(i) - ord("a"))            
        

    def encode(self, text):
        cipher = ""
        i = 0
        for x in text.lower():
            if x.isalpha():
                cipher += self.plain[ord(x)-ord("a") + self.count[i]]
                i += 1
                if i == len(self.count):
                    i = 0
            else:
                continue
            
        return cipher.rstrip()

    def decode(self, text):
        strplain = ""

        i = 0
        for x in text:
            if x.isalpha():
                strplain += self.plain[ord(x)-ord("a") + 26 - self.count[i]]
                i += 1
                if i == len(self.count):
                    i = 0
            else:
                continue
            
        return strplain
    
class Caesar(object):
    a = Cipher("d")
    def __init__(self):
        a = Cipher("d")
        
    def encode(self, text):
        return self.a.encode(text)
        
    def decode(self, text):
        return self.a.decode(text)
