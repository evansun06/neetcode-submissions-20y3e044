class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        """
        start: [0] * len(target)
        target: 
        minimum number of operations to reach the target array such that
        a single operation increments a single contiguous subarray

        [0,0,0,0,0]
        [1,1,1,1,1]
        [1,2,2,2,2]
        [1,2,3,2,2]
        [1,2,3,2,3]
        [1,2,3, 2,3]
            x   x
          x x x x x
        x x x x x x _ x
        """

        ops = target[0]

        for i in range(1, len(target)):
            if target[i-1] < target[i]:
                ops += (target[i] - target[i - 1])
        return ops
