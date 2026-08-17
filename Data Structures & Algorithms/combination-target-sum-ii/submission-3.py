class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []
        path = []
        candidates.sort()
        print(candidates)
        def dfs(n, sum):

            if sum == target:
                result.append(path.copy())
                return
       
            for next in range(n + 1, len(candidates)):

                    if next > n + 1 and candidates[next] ==  candidates[next-1]:
                        continue
                    if sum + candidates[next] > target:
                        break

                    path.append(candidates[next])
                    dfs(next, sum + candidates[next])
                    path.pop()

                    
        dfs(-1, 0)
        
        return result
        