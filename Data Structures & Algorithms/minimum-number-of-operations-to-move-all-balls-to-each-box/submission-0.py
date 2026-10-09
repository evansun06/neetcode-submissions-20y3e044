class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        """
        double loop 
        
        001011

        """
        balls = set()
        for i in range(len(boxes)):
            if boxes[i] == "1":
                balls.add(i)

        answer = [0] * len(boxes)

        for i in range(len(boxes)):
            for j in balls:
                answer[i] += abs(j - i)
        return answer
