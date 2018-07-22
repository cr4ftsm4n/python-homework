EQUAL = 1
SUPERLIST = 2
SUBLIST = 3
UNEQUAL = 4
def check_lists(first_list, second_list):
    if first_list == second_list:
        return EQUAL
    if len(first_list) > len(second_list):
        i = 0
        while i+len(second_list) <= len(first_list):
            if first_list[i:i+len(second_list)] == second_list:
                return SUPERLIST
            i += 1
    elif len(first_list) == len(second_list):
        return UNEQUAL
    else:
        i = 0
        while i+len(first_list) <= len(second_list):
            if second_list[i:i+len(first_list)] == first_list:
                return SUBLIST
            i += 1
    return UNEQUAL
