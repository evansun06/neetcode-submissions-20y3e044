class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        """
        Peaks and valleys: We will run a linear pass

        for i in range(len(target)):
            if n > 0 and target[n-1]<=target[n]:
                result += target[n-1]<=target[n]
        """

        res = target[0]

        for i in range(len(target)):
            if i > 0 and target[i - 1] <= target[i]:
                res += target[i] - target[i - 1]
        
        return res