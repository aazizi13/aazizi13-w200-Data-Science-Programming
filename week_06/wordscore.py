
def score_word(word, score):
    total = 0 
    for w in word:
        total= total + score[w.lower()]
    return total 
