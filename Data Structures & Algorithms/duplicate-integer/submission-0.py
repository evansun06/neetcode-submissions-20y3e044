class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = set()
        for i in nums:
            if i in unique:
                return True
            else:
                unique.add(i)

        return False
            
