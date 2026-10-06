from collections import defaultdict

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        """
        ["abc","bcd","acef","xyz","az","ba","a","z"]

        if we say a, b, c, ..., y, z = 1, 2, 3, ..., 25, 26

        (1 2 3), (1,2,3)

        grouped sequences relate by:
         - length
         - differences in character 
        """

        def hash(s: string):
            while s[0] != 'a':
                s = list(s)
                for i in range(len(s)):
                    s[i] = chr(97 + ((ord(s[i]) - 97 + 1) % 26))
            
            return "".join(s)

        hash_map = defaultdict(list)

        for s in strings:
            hash_map[hash(s)].append(s)
        
        return list(hash_map.values())

