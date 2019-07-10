import re, string
def is_pangram(sentence):
    """Determine if a sentence is a pangram. A pangram (every letter) 
    is a sentence using every letter of the alphabet at least once.
    Runtime: O(n) where n number of chars
    """
    
    # remove all chars/space except letters and lowercase them
    norm_sent = ''.join(filter(str.isalpha, sentence)).lower() # O(n)
    
    # create a set from the sentence
    norm_sent = set(norm_sent) # O(n)
    
    # check if all letters occured
    return len(norm_sent) == 26 # O(1)






sentence = "the quick brown fox jumps over the lazy dog"
print(is_pangram(sentence))
