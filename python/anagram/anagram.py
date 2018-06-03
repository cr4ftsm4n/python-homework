import copy
def detect_anagrams(word, candidates):
    lowerword = word.lower()
    h = [0] * 26
    
    a = []
    for ch in lowerword:
        h[ord(ch)-ord('a')] += 1
    
    for words in candidates:
        temp = copy.deepcopy(h)
        b = True
        lowerwords = str(words).lower()
        if lowerwords == lowerword:
            continue
        for ch in lowerwords:
            if ch.isalpha():
                temp[ord(ch)-ord('a')] -= 1
        for elem in temp:
            if elem != 0:
                b = False
                break
                
        if b == True:
            a.append(words)
        else:
            continue
    
    return a
