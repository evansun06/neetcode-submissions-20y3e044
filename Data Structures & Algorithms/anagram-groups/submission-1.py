from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            key = str(sorted(s))
            groups[key].append(s)
        
        return [groups[key] for key in groups]