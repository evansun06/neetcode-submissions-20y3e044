class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        s = strs[0]

        for i in range(len(s)):
            for candidate in strs:
                if i < len(candidate) and candidate[i] != s[i]:
                    return s[:i]
                elif i >= len(candidate):
                    return candidate
        return s