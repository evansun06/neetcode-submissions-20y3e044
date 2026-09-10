class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        shortest = None

        for s in strs:
            if shortest is None or len(shortest) > len(s):
                shortest = s
        
        pre = ""
        for i in range(len(shortest)):
            for s in strs:
                if s[i] != shortest[i]:
                    return pre
            
            pre = shortest[:i + 1]

        return pre
            
            
        