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

        def backtrack(i: int, path: str):
            if i == len(digits):
                result.append(path)
                return
            
            for char in digits_map[digits[i]]:
 
                backtrack(i + 1, path + char)

        backtrack(0, "")

        return result if len(digits) > 0 else []