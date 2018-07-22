from collections import Sequence

def flatten_helper(lst, new_lst):
    for element in lst:
        if isinstance(element, list):
            flatten_helper(element, new_lst)
        else:
            if element == None or (isinstance(element, Sequence) and len(element) == 0):
                continue
            else:
                new_lst.append(element)

def flatten(iterable):
    new_lst = []
    flatten_helper(iterable, new_lst)
    return new_lst
