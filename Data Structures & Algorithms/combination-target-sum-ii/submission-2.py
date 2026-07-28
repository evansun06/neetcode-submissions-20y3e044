class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        candidates.sort()
        solution = []
        def backtrack(sum: int, i: int):
            if sum == target:
                solution.append(path.copy())
                return

            if sum > target or i == len(candidates):
                return
            
            path.append(candidates[i])
            backtrack(sum + candidates[i], i + 1)
            
            path.pop()

            # Exclude candidates[i] and all identical sibling choices
            next_i = i + 1

            while (
                next_i < len(candidates)
                and candidates[next_i] == candidates[i]
            ):
                next_i += 1

            backtrack(sum, next_i)

        
        backtrack(0, 0)

        return solution