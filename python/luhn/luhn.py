class Luhn(object):
    card_num = ""
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ","")

    def is_valid(self):
        total = 0
        if self.card_num.isdigit() and len(self.card_num) > 1:
            i = 1
            for x in self.card_num[::-1]:
                num = int(x)
                if i%2 == 0:
                    if num*2 >=10:
                        total += (num*2 - 9)
                    else:
                        total += (num*2)
                else:
                    total += num
                i += 1
        else:
            total = 1
        
        if total%10 == 0:
            return True
        else:
            return False
                        
