from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        need = Counter(s1)
        window = Counter()
        left = 0
        k = len(s1)

        for right, ch in enumerate(s2):
            window[ch] += 1

            if right > (k - 1):
                window[s2[left]] -= 1
                if window[s2[left]] == 0:
                    del window[s2[left]]
                left += 1

            if window == need:
                return True
        
        return False

