ACTIONS = ['wink', 'double blink', 'close your eyes', 'jump']

def handshake(code):
    l = []
    num = code
    while True:
        num, remainder = divmod(num, 2)
        l.append(remainder)
        if num == 0:
            break
            
    shake = []
    for i in range(0,len(l)):
        if l[i] == 1:
            if i == 4:
                shake = shake[::-1]
            else:
                shake.append(ACTIONS[i])
                
    return shake
        


def secret_code(actions):
    code = 0
    for action in actions:
        if action == ACTIONS[0]:
            code += 1
        elif action == ACTIONS[1]:
            code += 2
        elif action == ACTIONS[2]:
            code += 4
        elif action == ACTIONS[3]:
            code += 8
    return code
