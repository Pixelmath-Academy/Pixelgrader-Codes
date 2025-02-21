def are_words_same(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    
    if word1 == word2:
        return "YES"
    
    def one_letter_missing(w1, w2):
        if len(w1) + 1 != len(w2):
            return False
        for i in range(len(w2)):
            if w1 == w2[:i] + w2[i+1:]:
                return True
        return False
    
    def adjacent_letters_reversed(w1, w2):
        if len(w1) != len(w2):
            return False
        for i in range(len(w1) - 1):
            if w1[i] == w2[i+1] and w1[i+1] == w2[i]:
                if w1[:i] + w1[i+2:] == w2[:i] + w2[i+2:]:
                    return True
        return False
    
    def one_letter_excess(w1, w2):
        return one_letter_missing(w2, w1)
    
    conditions_met = 0
    if one_letter_missing(word1, word2):
        conditions_met += 1
    if adjacent_letters_reversed(word1, word2):
        conditions_met += 1
    if one_letter_excess(word1, word2):
        conditions_met += 1
    
    if conditions_met == 1:
        return "YES"
    return "NO"

input_line = input().strip()
word1, word2 = input_line.split()

print(are_words_same(word1, word2))