def translate_word(word):
    if word[0] in "aeiou":
        return word + "ay"
    elif word[0] in "xy" and not (word[1] in "aeiou"):
        return word + "ay"
    elif len(word) > 3 and word[0:3] in ["str", "squ", "sch", "thr"]:
        return word[3:] + word[0:3] + "ay"
    elif len(word) > 2 and word[0:2] in ["ch", "sh", "sm", "st", "th", "gl", "qu", "rh"]:
        return word[2:] + word[0:2] + "ay"
    else:
        return word[1:] + word[0] + "ay"


def translate(text):
    words = text.split()
    result = []
    for word in words:
        result.append(translate_word(word))
    return " ".join(result)
