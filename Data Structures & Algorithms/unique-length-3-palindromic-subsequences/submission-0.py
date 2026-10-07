from collections import defaultdict

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        """
        Brute force:
        triple loop, looking at all possible triplets i,j,k
        where i j k form a palindrome

        Add to a set to reduce duplicates.

        "xaabca"

        "a*a" - "aca", "aba", "aaa"
        """

        res = set()

        occurances = defaultdict(list)

        for i in range(len(s)):
            occurances[s[i]].append(i)
        
        for c in occurances:
            if len(occurances[c]) >= 2:
                left, right = occurances[c][0], occurances[c][-1]

                for i in range(left + 1, right):
                    res.add(c+s[i]+c)
        return len(res)
    
                        

                