from itertools import combinations
class Allergies(object):
    score = 0
    dic = {"eggs":1, "peanuts":2, "shellfish":4, "strawberries":8, "tomatoes":16, "chocolate":32, "pollen":64, "cats":128}
    lista = ["eggs", "peanuts", "shellfish", "strawberries", "tomatoes", "chocolate", "pollen", "cats"]

    def __init__(self, score):
        Allergies.score = score

    def is_allergic_to(self, item):
        
        if Allergies.score >= Allergies.dic[item]:
            return True
        else:
            return False

    @property
    def lst(self):
        binself = bin(Allergies.score)
        
        listallergies = []
        index = 0
        for i in binself[::-1]:
            if index < len(Allergies.lista):
                if i == "1":
                    listallergies.append(Allergies.lista[index])
                    index += 1
                elif i == "b":
                    break
                else:
                    index += 1
                    continue
            else:
                break
            
            
        return listallergies
                
