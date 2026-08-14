class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        def expand_odd(i, s: str) -> int:
            x = 0
            while (i + x < len(s)) and (i - x >= 0):
                if s[i+x] == s[i-x]:
                    x += 1
                else:
                    break

            return x
                    

        def expand_even(left, right, s):
            x = 0
            while (right + x < len(s)) and (left - x >= 0):
                if s[right + x] == s[left - x]:
                    x += 1
                else:
                    break
            return x


        for i in range(len(s)):
            
            # odd mid
            count += expand_odd(i, s)

            if(i != len(s) - 1):
                count += expand_even(i, i + 1, s)
        
        return count

