class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Sliding window O(n)
        We iterate through the entire string:
        - at each character, we check if its a duplicate:
        - while the character is still in the substring, we remove charaters at our left pointer
          from the set until only 1 of each remains.

        """

        state = set()
        left = 0
        best = 0
        for right in range(len(s)):

            while s[right] in state:
                state.remove(s[left])
                left += 1
            
            state.add(s[right])
            best = max(best, len(state))
        
        return best
