class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        """
        first = [[0,2],[5,10],[13,23],[24,25]]
        second = [[1,5],[8,12],[15,24],[25,26]]

        let i, j represent traversal through firstList and secondList respectively

        [1,5]
        [3,3]
        if first[i][0] <= second[i][0]:
            if first[i][1] <= second[i][0]:
                intersection = [second[i][0], min(second[i][0], first[i][0]]
        else
        """
        
        len1 = len(firstList)
        len2 = len(secondList)

        i = 0
        j = 0

        res = []
        while i < len1 and j < len2:
            if firstList[i][1] >= secondList[j][0] and secondList[j][1] >= firstList[i][0]:       
                if firstList[i][0] <= secondList[j][0]:
                    intersection = [secondList[j][0], min(secondList[j][1], firstList[i][1])]
                else:
                    intersection = [firstList[i][0], min(secondList[j][1], firstList[i][1])]
                    
                res.append(intersection)
            
            if firstList[i][1] <= secondList[j][1]:
                i += 1
            else:
                j += 1

            
        return res