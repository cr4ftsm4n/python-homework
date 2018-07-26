def handshake(code):
    actions = []
    if code & 1 != 0:
        actions.append("wink")
    if code & 2 != 0:
        actions.append("double blink")
    if code & 4 != 0:
        actions.append("close your eyes")
    if code & 8 != 0:
        actions.append("jump")
    if code & 16 != 0:
        actions = actions[::-1]
    return actions


def secret_code(actions):
    total = 0
    possible = ["wink", "double blink", "close your eyes", "jump"]
    for action in actions:
        if action in possible:
            idx = possible.index(action)
            total += 2 ** (idx)
    if len(actions) > 1:
        fst = actions[0]
        sec = actions[1]
        if possible.index(fst) > possible.index(sec):
            total += 16
    return total
