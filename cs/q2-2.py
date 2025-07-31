"""
Given a list of words (consisting of lowercase English letters) and a complex word written in camelCase 
(consisting of English letters), check if the complex word consists of words from the given list.
"""
def consistsOfWords(words, complexWord):
    # Convert words list to a set for O(1) lookup and lowercase
    word_set = set(words)
    start = 0
    parts = []
    
    for i in range(1,len(complexWord)):
        if complexWord[i].isupper():
            parts.append(complexWord[start:i].lower())
            start = i
            
    parts.append(complexWord[start:].lower())

    for part in parts:
        if part in word_set:
            return True
        
    return False   
    
print(consistsOfWords(["test","me"], "CanMeDoTest"))
print(consistsOfWords(["test","me"], "HowManyTimesCanIDoThisMe"))
print(consistsOfWords(["test","me"], "Te"))
print(consistsOfWords(["test","me"], "TestMe"))