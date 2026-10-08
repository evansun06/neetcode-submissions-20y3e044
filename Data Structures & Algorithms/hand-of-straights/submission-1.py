class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """
        1,2,4,2,3,5,3,4

        1 = 1
        2 = 2
        3 = 2
        4 = 2
        5 = 1
        """
        if len(hand) % groupSize != 0:
            return False
        

        count = Counter(hand)

        for key in sorted(count):
            while count[key] > 0:
                for i in range(key, key + groupSize):
                    if count[i]:
                        count[i] -= 1
                    else:
                        return False
        
        return True
                        
                        
            

        