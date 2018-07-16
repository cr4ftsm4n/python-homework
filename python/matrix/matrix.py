class Matrix(object):
    matrix_list = []
    def __init__(self, matrix_string):
        self.matrix_list = []
        matrix_list = matrix_string.split("\n")
        for i in matrix_list:
            self.matrix_list.append(i.split(" "))

    def row(self, index):
        row_list = []
        for i in self.matrix_list[index]:
            row_list.append(int(i))
            
        return row_list

    def column(self, index):
        column_list = []
        for i in self.matrix_list:
            column_list.append(int(i[index]))
            
        return column_list
