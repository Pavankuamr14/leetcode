from collections import Counter
from typing import List

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # Calculate the maximum frequency of each character in all words2
        max_freq = Counter()
        for word in words2:
            word_count = Counter(word)
            for char in word_count:
                max_freq[char] = max(max_freq[char], word_count[char])
                print(max_freq)
        
        # Check for universal words in words1
        result = []
        for word in words1:
            word_count = Counter(word)
            if all(word_count[char] >= max_freq[char] for char in max_freq):
                result.append(word)
        
        return result
