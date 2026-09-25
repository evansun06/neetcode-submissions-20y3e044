class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
            left right pointers, with a delete flag
            if delete flag is false and we encounter non matching characters:
                - allow once and only increment the
        """

        def isPalindrome(left: int, right: int, s: str):
            while left <= right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    return False
            return True

        left, right = 0, len(s) - 1

        while left <= right:
            if s[left] != s[right]:
                return (
                    isPalindrome(left, right - 1, s)
                    or isPalindrome(left + 1, right, s)
                )
            else:
                left += 1
                right -= 1
        
        return True
        
        