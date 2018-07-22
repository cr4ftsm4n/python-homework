open_brackets = '([{'
close_brackets = ')]}'
brackets_map = {')': '(', ']': '[', '}': '{'}
def is_paired(input_string):
    stack = []
    label = True
    for char in input_string:
        if char in open_brackets:
            stack.append(char)
        elif char in close_brackets:
            if len(stack) < 1:
                label = False
                break
            elif brackets_map[char] == stack[-1]:
                stack.pop()
            else:
                label = False
                break
        else:
            continue
    if stack != []:
        label = False
        
    return label
