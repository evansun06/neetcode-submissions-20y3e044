class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        i = 0
        while i < len(s):

            not_end = True if i < len(s) - 1 else False
            match s[i]:
                case "I":
                    if not_end and s[i+1] == "V":
                        i += 1
                        result += 4
                    elif not_end and s[i+1] == "X":
                        i += 1
                        result += 9
                    else:
                        result += 1
                      
                case "V":
                    result += 5 
                case "X":
                    if not_end and s[i+1] == "L":
                        i += 1
                        result += 40
                    elif not_end and s[i+1] == "C":
                        i += 1
                        result += 90
                    else:
                        result += 10
                case "L":
                    result += 50
                case "C":
                    if not_end and s[i+1] == "D":
                        i += 1
                        result += 400
                    elif not_end and s[i+1] == "M":
                        i += 1
                        result += 900
                    else:
                        result += 100
                case "D":
                    result += 500
                case "M":
                    result += 1000
                
            i += 1
        return result