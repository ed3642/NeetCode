import re

class Solution:
    def isValid(self, word: str) -> bool:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        alphabet = alphabet + alphabet.upper()
        consonants = 'aeiouAEIOU'
        nonvowel = ''.join(set(alphabet) - set(consonants))

        if len(word) < 3:
            return False
        
        # chars or nums
        if not re.match("^[a-zA-Z0-9]+$", word):
            return False
        
        # at least one vowel
        if not re.search('[aeiouAEIOU]', word):
            return False
        
        # at least one non-vowel
        if not re.search(f'[{nonvowel}]', word):
            return False
        
        return True
        
