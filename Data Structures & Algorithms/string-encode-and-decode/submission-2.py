class Solution:
    """
        H*E*L*L*Ox
    """

    def encode(self, strs: List[str]) -> str:
        result = []

        for string in strs:
            length = len(string)

            if length < 10:
                result.append("00" + str(length) + string)
            elif length < 100:
                result.append("0" + str(length) + string)
            else:
                result.append(str(length) + string)
        
        result =  "".join(result)
        print(result)
        return result
        

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            length = int(s[i: i + 3])
            word = s[i + 3: i + 3 + length]
            result.append(word)
            i = i + 3 + length
        return result


