from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        t_state = defaultdict(int)

        for i in range(len(t)):
            t_state[t[i]] += 1

        counter = defaultdict(int)

        have = 0
        need = len(t_state)

        result = None
        left = 0

        for right in range(len(s)):


            if s[right] in t_state:
                counter[s[right]] += 1

                if counter[s[right]] == t_state[s[right]]:
                    have += 1

            while have == need:
                if result is None or len(result) > right - left + 1:
                    result = s[left:right + 1]

                if s[left] in t_state:
                    if counter[s[left]] == t_state[s[left]]:
                        have -= 1
                        
                    counter[s[left]] -= 1

                
                left += 1
        
        return result if result is not None else ""



