class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # ababd
        longestPalindrome = s[0]


        for i in range(len(s)):

            left, right = 0, 0
            while i - left >= 0 and i + right < len(s):
                if s[i - left] == s[i + right]:
                    p = s[(i - left): (i + right + 1)]
                    
                    if len(p) > len(longestPalindrome):
                        longestPalindrome = p
                    
                    left += 1
                    right += 1
                else:
                    break

            if i != len(s) - 1:
                left = i
                right = i + 1

                while left >= 0 and right < len(s):

                    if s[left] == s[right]:
                        
                        p = s[left: right + 1]
                        if len(p) > len(longestPalindrome):
                            longestPalindrome = p

                        left -= 1
                        right += 1
                    else:
                        break
    
        return longestPalindrome


        