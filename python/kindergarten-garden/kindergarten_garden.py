class Garden(object):
    dic_name_plants = {}
    list_name = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]
    dic_plants = {"G":"Grass", "C":"Clover", "R":"Radishes", "V":"Violets"}    
    def __init__(self, diagram, students=[]):
        if len(students) > 0:
            self.list_name = students
            self.list_name.sort()
            
        list_diagram = diagram.split("\n")
        
        i_diagram = 0
        i_name = 0
        while i_diagram < len(list_diagram[0]):
            self.dic_name_plants[self.list_name[i_name]] = list_diagram[0][i_diagram] + list_diagram[0][i_diagram+1] + list_diagram[1][i_diagram] + list_diagram[1][i_diagram+1]
            i_diagram += 2
            i_name += 1
            
    def plants(self, name):
        str_plants = ""
        for i in self.dic_name_plants[name]:
            str_plants += self.dic_plants[i] + " "
            
        return str_plants.split()
            
