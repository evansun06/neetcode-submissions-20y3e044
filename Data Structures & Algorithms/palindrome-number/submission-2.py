class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        cast x -> string
        return x == x[::-1]
        """

        x = str(x)
        return x == x[::-1]