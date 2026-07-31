class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        path = [s[0]]

        def backtrack(i):
            # i fast, j slow
            if i == len(s):
                if path[-1] == path[-1][::-1]:
                    result.append(path.copy())
                return

            if path[-1] == path[-1][::-1]:
                path.append(s[i])
                backtrack(i + 1)
                path.pop()

            path[-1] = path[-1] + s[i]
            backtrack(i + 1)
            path[-1] = path[-1][:-1]
            
        backtrack(1)
        return result
