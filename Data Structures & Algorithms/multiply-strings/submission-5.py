class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        len1, len2 = len(num1), len(num2)
        res = [0] * (len1 + len2)

        for i in range(len1 - 1, -1, -1):
            for j in range(len2 - 1, -1, -1):
                val = int(num1[i]) * int(num2[j])
                val += res[i + j + 1]

                res[i + j + 1] = val % 10
                res[i + j] += val // 10

        beg = 0
        while beg < (len1 + len2) and res[beg] == 0:
            beg += 1
        res = "".join(map(str, res[beg:]))
        return res if res != "" else "0"




