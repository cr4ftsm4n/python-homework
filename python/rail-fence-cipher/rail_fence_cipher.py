def encode(message, rails):
    cipher = ''

    length = len(message)
    fence = [['#']*length for _ in range(rails)]

    rail = 0
    for x in range(length):
        fence[rail][x] = message[x]
        if rail >= rails-1:
            dr = -1
        elif rail <= 0:
            dr = 1
        rail += dr

    for rail in range(rails):
        for x in range(length):
            if fence[rail][x] != '#':
                cipher += fence[rail][x]
    return cipher


def decode(encoded_message, rails):
    plain = ''
    
    length = len(encoded_message)
    fence = [['#']*length for _ in range(rails)]

    i = 0
    for rail in range(rails):
        p = (rail != (rails-1))
        x = rail
        while (x < length and i < length):
            fence[rail][x] = encoded_message[i]
            if p:
                x += 2*(rails - rail - 1)
            else:
                x += 2*rail
            if (rail != 0) and (rail != (rails-1)):
                p = not p
            i += 1

    for i in range(length):
        for rail in range(rails):
            if fence[rail][i] != '#':
                plain += fence[rail][i]
    return plain
