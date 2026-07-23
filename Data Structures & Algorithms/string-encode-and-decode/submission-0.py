class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            length = len(s)
            if length < 10:
                result += ("00" + str(length))
            elif length < 100:
                result += ("0" + str(length))
            else:
                result += str(length)

            result += s

        return result
            

    def decode(self, s: str) -> List[str]:
        result = []
        x = 0
        while x < len(s):
            length = int(s[x: x + 3])
            if length == 0:
                result.append("")
            else:
                string = s[x + 3: x + 3 + length]
                result.append(string)
            x = x + 3 + length
            
        return result
            



