from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        counter = defaultdict(int)
        left = 0
        mostFreq = 0
        res = 0
    
        for right in range(len(s)):
            counter[s[right]] += 1
            mostFreq = max(mostFreq, counter[s[right]])

            while right - left + 1 - mostFreq > k:
                counter[s[left]] -= 1
                left += 1
                
            if right - left + 1 > res:
                res = right - left + 1
        
        return res


        