class Solution:
    def reverse(self, x: int) -> int:
        """
        overflow happens when sign change
        """

        num = x if x >= 0 else -x
        rev = 0

        while num:
            rev = (rev * 10) + num % 10
            num //= 10
        
        rev = rev if x >= 0 else -rev

        if -2**31 <= rev <= 2**31 - 1:
            return rev
        else:
            return 0

        

        
