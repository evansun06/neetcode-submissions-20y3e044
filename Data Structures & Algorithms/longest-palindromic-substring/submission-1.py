class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        we consider both the odd and even palindrome start cases:
        - odd -> left right = i
        - even -> left = i right = i + 1
        """
        longest = s[0]

        def isPalindrome(l, r):
            nonlocal longest
            while 0 <= l and r < len(s):
                if s[l] == s[r]:
                    candidate = s[l:r + 1]
                    if len(candidate) > len(longest):
                        longest = candidate
                    l -= 1
                    r += 1
                else:
                    return

        for i in range(len(s)):

            # odd
            isPalindrome(i, i)

            if i == len(s) - 1:
                continue
            
            # even
            isPalindrome(i, i + 1)
            
        return longest