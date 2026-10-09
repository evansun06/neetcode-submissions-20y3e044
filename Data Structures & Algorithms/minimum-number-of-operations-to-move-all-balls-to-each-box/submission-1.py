class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        answer = [0] * len(boxes)
        balls = 0
        moves = 0
        for i in range(len(boxes)):
            answer[i] = balls + moves
            moves = balls + moves

            if boxes[i] == "1":
                balls += 1
        
        balls = 0
        moves = 0

        for i in range(len(boxes)-1, -1, -1):
            answer[i] += (balls + moves)
            moves = balls + moves

            if boxes[i] == "1":
                balls += 1

        
        return answer