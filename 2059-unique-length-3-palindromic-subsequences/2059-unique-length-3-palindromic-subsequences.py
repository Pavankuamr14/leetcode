class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        unique = set(s)
        ans = 0
        
        for letter in unique:
            i, j = s.index(letter), s.rindex(letter)
            holder = set()
            
            for k in range(i + 1, j):
                holder.add(s[k])

            ans += len(holder)
        return ans
        # unique_palindromes = set()
        # for i in range(1, len(s) - 1):  
        #     left_chars = set(s[:i])
        #     right_chars = set(s[i+1:])
        #     for char in left_chars:
        #         if char in right_chars:
        #             unique_palindromes.add(char + s[i] + char)
        # return len(unique_palindromes)


#         n = len(s)
#         unique_palindromes = set()

#         # using powerset
#         for i in range(1, 1 << n):  # 1 to 2^n - 1 (skipping the empty set)
#             subsequence = ''
#             for j in range(n):
#                 if i & (1 << j):  
#                     subsequence += s[j]
#             if len(subsequence) == 3 and self.is_palindrome(subsequence):
#                 unique_palindromes.add(subsequence)

#         return len(unique_palindromes)

#     def is_palindrome(self, text: str) -> bool:
#         return text == text[::-1]  