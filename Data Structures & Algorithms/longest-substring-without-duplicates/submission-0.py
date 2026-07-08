class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_len = 0
        char_set = set()
        
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.discard(s[left])
                left += 1
            
            char_set.add(s[right])

            if len(char_set) > max_len:
                max_len = len(char_set)

        return max_len