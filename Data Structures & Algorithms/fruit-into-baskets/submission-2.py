class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """
        looking for the longest contiguous subarry with only two types of trees

        [0,1,2,2]

        
        [0,1,2,2,0]
        """
        start = 0
        maximum_fruits = 0
        fruit_types = {}
        for right in range(len(fruits)):
            if fruits[right] not in fruit_types:
                fruit_types[fruits[right]] = 1
            else:
                fruit_types[fruits[right]] += 1

            while len(fruit_types) > 2:
                if fruits[start] in fruit_types:
                    fruit_types[fruits[start]] -= 1
                    if fruit_types[fruits[start]] == 0:
                        del fruit_types[fruits[start]]
                start += 1
            
            maximum_fruits = max(maximum_fruits, right - start + 1)

        return maximum_fruits
            

            


