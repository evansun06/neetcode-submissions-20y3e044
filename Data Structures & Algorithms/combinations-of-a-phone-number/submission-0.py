class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        result = []
        path = []
        def backtrack(i: int):
            if i == len(digits):
                result.append("".join(path))
                return
            
            for char in digits_map[digits[i]]:
                path.append(char)
                backtrack(i + 1)
                path.pop()
        
        backtrack(0)

        return result if len(digits) > 0 else []