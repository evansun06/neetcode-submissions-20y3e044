class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        def backtrack(i, path):
            if i == len(nums):
                result.append(path.copy())
                return
            
            
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

            next_i = i + 1

            while (next_i < len(nums) and nums[next_i] == nums[i]):
                next_i +=1
            
            backtrack(next_i, path)
        
        backtrack(0, [])
        return result

            