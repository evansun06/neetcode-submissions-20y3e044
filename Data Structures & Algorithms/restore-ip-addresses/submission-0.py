class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def dfs(i, dotsPlaced, ip):
            if dotsPlaced == 3:
                part = s[i:]
                if not part or len(part) > 3:
                    return
                if len(part) > 1 and part[0] == "0":
                    return
                if 0 <= int(part) <= 255:
                    res.append(ip + part)
                return

            if i >= len(s):
                return

            if s[i] == "0":
                dfs(i + 1, dotsPlaced + 1, ip + s[i] + ".")
            else:
                for end in range(i + 1, min(i + 4, len(s) + 1)):
                    if 0 <= int(s[i:end]) <= 255:
                        dfs(end, dotsPlaced + 1, ip + s[i:end] + ".")
        
        dfs(0, 0, "")
        return res