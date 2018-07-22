def score(word):
    score = 0
    upper_word = word.upper()
    dic = {"AEIOULNRST":1,"DG":2, "BCMP":3, "FHVWY":4, "K":5, "JX":8, "QZ":10}
    for i in upper_word:
        for key in dic:
            if key.find(i) != -1:
                score += dic[key]
    return score
