class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Sliding Window

        set = {z,x,y}
        "zxyzxyz"
           l
             x
        """

        left = 0
        longest = 0
        window = set()

        for right in range(len(s)):

            while s[right] in window and left < right:
                window.remove(s[left])
                left += 1

            window.add(s[right])
            longest = max(longest, right - left + 1)
            
        
        return longest
            
