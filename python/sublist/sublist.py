EQUAL = 0
SUBLIST = 1
SUPERLIST = 2
UNEQUAL = 3


def contains(long_list, short_list):
    if len(short_list) == 0:
        return True
    else:
        first = short_list[0]
        indice = [i for i, d in enumerate(long_list) if d == first]
        length = len(short_list)
        for i in indice:
            if len(long_list[i:]) >= length:
                if long_list[i: i + length] == short_list:
                    return True
        return False


def check_lists(first_list, second_list):
    if len(first_list) == len(second_list):
        if first_list == second_list:
            return EQUAL
        else:
            return UNEQUAL
    if len(first_list) > len(second_list):
        if contains(first_list, second_list):
            return SUPERLIST
        else:
            return UNEQUAL
    else:
        if contains(second_list, first_list):
            return SUBLIST
        else:
            return UNEQUAL
