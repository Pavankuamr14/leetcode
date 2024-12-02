class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        holder=sentence.split(' ')
        for word in range(len(holder)):
            if holder[word][:len(searchWord)]==searchWord:
                return word+1
        return -1
                
            