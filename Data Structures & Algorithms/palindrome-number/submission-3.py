class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        reverse number numerically:
        num = x
        rev = 0
        
        while num:
            rev = rev * 10 + num // 10
            num //= 10
        """
        if x < 0:
            return False
            
        num = x
        rev = 0
        while num:
            rev = (rev*10) + (num % 10)
            num = num // 10


        return rev == x