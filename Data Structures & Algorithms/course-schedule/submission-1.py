from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj_list = defaultdict(list)
        in_ord = [0] * numCourses

        for post, pre in prerequisites:
            adj_list[pre].append(post)
            in_ord[post] += 1
        
        q = deque()
        for i in range(len(in_ord)):
            if in_ord[i] == 0:
                q.append(i)

        count = 0
        while q:
            course = q.popleft()
            count += 1

            for next_course in adj_list[course]:
                in_ord[next_course] -= 1
                if in_ord[next_course] == 0:
                    q.append(next_course)
        

        return True if count == numCourses else False
        