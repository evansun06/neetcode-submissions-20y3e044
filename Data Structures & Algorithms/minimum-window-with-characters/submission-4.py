from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        counter_t = Counter(t)
        counter_s = Counter()

        min_left = 0
        min_length = float("inf")
        left = 0

        def valid_window() -> bool:
            return all(
                counter_s[char] >= required_count
                for char, required_count in counter_t.items()
            )

        for right, char in enumerate(s):
            if char in counter_t:
                counter_s[char] += 1
            
            while valid_window() and left <= right:
                if (right - left + 1) < min_length:
                    min_length = right - left + 1
                    min_left = left
                
                if s[left] in counter_s:
                    counter_s[s[left]] -= 1
                    
                left += 1
        
        if min_length == float("inf"):
            return ""

        return s[min_left: min_left + min_length]
            