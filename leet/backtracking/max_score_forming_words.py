from collections import Counter

class Solution:
    def maxScoreWords(self, words: list[str], letters: list[str], score: list[int]) -> int:
        # preprocess the val of words
        # consider taking all combinations and see which one wins
        # restrict paths with letters availability

        def backtrack(start, score):
            nonlocal max_score
            max_score = max(max_score, score)

            if start >= len(words):
                return score
            
            for i in range(start, len(words)):
                word = word_letters_needed[i] # rep as its chars freqs
                if can_build_word(word):
                    new_score = score + word_val[i]
                    account_letters(word, True)
                    backtrack(i + 1, new_score)
                    account_letters(word, False)

        def account_letters(letters, spending=True):
            if spending:
                for ch, freq in letters.items():
                    letters_available[ch] -= freq
            else:
                for ch, freq in letters.items():
                    letters_available[ch] += freq

        def can_build_word(letters_needed):
            return False if any(letters_needed[ch] > letters_available[ch] for ch in letters_needed) else True

        def calc_word_val(word):
            total = 0
            for ch in word:
                total += ch_val[ch]
            return total

        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        ch_val = dict(zip(alphabet, score))
        word_val = [] # same order as words arr
        word_letters_needed = []
        for word in words:
            word_val.append(calc_word_val(word))
            word_letters_needed.append(Counter(word))
        letters_available = Counter(letters)

        max_score = 0
        backtrack(0, 0)
        return max_score        