from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        in_orders = [0] * numCourses
        impact_map = [ [] for _ in range(numCourses)]

        for post, pre in prerequisites:
            in_orders[post] += 1
            impact_map[pre].append(post)
        

        q = deque()
        for course, in_deg in enumerate(in_orders):
            if in_deg == 0:
                q.append(course)


        result = []

        while q:
            course = q.popleft()
            print(course)
            result.append(course)

            for post in impact_map[course]:
                if in_orders[post] - 1 == 0:
                    q.append(post)
                
                in_orders[post] -= 1
        
        return result if len(result) == numCourses else []

        

        