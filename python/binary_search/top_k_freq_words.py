# https://leetcode.com/problems/top-k-frequent-words
from collections import Counter

class Solution:
    # interesting use of quickselect but in this case since we have to
    # compare 2 values in the partitioner
    # and then sort the results anyways, we should just use a heap
    def topKFrequent(self, words: list[str], k: int) -> list[str]:

        def partitioner_lt_comparer(a, b):
            freq_a = freqs[unique_words[a]]
            freq_b = freqs[unique_words[b]]
            if freq_a < freq_b:
                return True
            if freq_a == freq_b and unique_words[a] > unique_words[b]:
                return True
            return False
        
        def partition(l, r, arbitrary_i):
            placer_i = l
            for i in range(l, r):
                if partitioner_lt_comparer(i, arbitrary_i):
                    unique_words[i], unique_words[placer_i] = unique_words[placer_i], unique_words[i]
                    placer_i += 1
            
            unique_words[r], unique_words[placer_i] = unique_words[placer_i], unique_words[r]

            return placer_i

        def quickselect(l, r):
            if l == r:
                return
            
            pivot_i = partition(l, r, r)

            if KTH_MOST_FREQ_INDEX == pivot_i:
                return
            elif KTH_MOST_FREQ_INDEX < pivot_i:
                quickselect(l, pivot_i - 1)
            else:
                quickselect(pivot_i + 1, r)

        freqs = Counter(words)
        unique_words = list(freqs.keys())
        N = len(unique_words)
        KTH_MOST_FREQ_INDEX = N - k
        quickselect(0, N - 1)
        
        # format output
        most_freq = unique_words[KTH_MOST_FREQ_INDEX:]
        words_with_freqs = sorted([(freqs[word], word) for word in most_freq], key=lambda x: (-x[0], x[1]))
        return [word for _, word in words_with_freqs]