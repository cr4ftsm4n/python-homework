class School(object):
    school_name = ""
    dic_roster = {1:set(),2:set(),3:set(),4:set(),5:set(),6:set(),7:set(),8:set(),9:set()}
    def __init__(self, name):
        self.school_name = name
        for n in range(1, 9):
            self.dic_roster[n] = set()
    
    def add(self, name, grade):
        self.dic_roster[grade].add(name)
        
    def grade(self, grade):
        return self.dic_roster[grade]
    
    def sort(self):
        list_name = []
        for n in range(1, 9):
            if self.dic_roster[n] == set():
                continue
            else:
                b = tuple(self.dic_roster[n])
                tuple_example = (n, b)
                list_name.append(tuple_example)
        return list_name
