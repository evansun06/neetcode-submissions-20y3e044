class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        we consider both the odd and even palindrome start cases:
        - odd -> left right = i
        - even -> left = i right = i + 1
        """
        best_len = 0
        best_start = 0

        def isPalindrome(l, r):
            nonlocal best_len, best_start
            
            while 0 <= l and r < len(s) and s[l] == s[r]:
                curr_len = r - l + 1
                if curr_len > best_len:
                    best_len = curr_len
                    best_start = l
                l -= 1
                r += 1


        for i in range(len(s)):

            # odd
            isPalindrome(i, i)
            
            # even
            isPalindrome(i, i + 1)
            
        return s[best_start:best_start + best_len]