from random import choice


class Cipher(object):
    def __init__(self, key=None):
        if key == None:
            candidats = "abcdefghijklmnopqrstuvwxyz"
            steps = []
            for i in range(0, 100):
                steps.append(choice(candidats))
            self.key = "".join(steps)
        else:
            for c in key:
                if c < "a" or c > "z":
                    raise ValueError("bad key")
            self.key = key

    def encode(self, text):
        result = ""
        mul = (len(text) // len(self.key) + 1)
        for (k, v) in zip(self.key * mul, text.lower()):
            if "a" <= v <= "z":
                new_ord = ord(v) + ord(k) - ord('a')
                if new_ord > ord("z"):
                    new_ord = ord("a") + new_ord - ord("z") - 1
                result += chr(new_ord)
        return result

    def decode(self, text):
        result = ""
        mul = (len(text) // len(self.key) + 1)
        for (k, v) in zip(self.key * mul, text):
            new_ord = ord(v) - (ord(k) - ord('a'))
            if new_ord < ord("a"):
                new_ord = ord("z") - ord("a") + new_ord + 1
            result += chr(new_ord)
        return result


class Caesar(Cipher):
    def __init__(self):
        super().__init__("d")
