from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        """
        
        x x R x R 

        i = 4
        d = 0
        r = 1
        """

        dire = deque()
        radiant = deque()

        for i in range(len(senate)):
            if senate[i] == "R":
                radiant.append(i)
            else:
                dire.append(i)
        
        while dire and radiant:
            if dire[0] > radiant[0]:
                dire.popleft()
                radiant.append(radiant.popleft() + len(senate))
            else:
                radiant.popleft()
                dire.append(dire.popleft() + len(senate))

        
        return "Dire" if dire else "Radiant"
