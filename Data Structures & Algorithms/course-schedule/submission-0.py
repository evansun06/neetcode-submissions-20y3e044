from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree_map = defaultdict(int)
        children_map = defaultdict(list)

        for p in prerequisites:
            post = p[0]
            pre = p[1]

            in_degree_map[post] += 1
            children_map[pre].append(post)
        

        q = deque()
        for course in range(numCourses):
            if in_degree_map[course] == 0:
                q.append(course)
        
        count = 0
        print(in_degree_map)
        print(children_map)
        while q:
            count += 1
            course = q.popleft()
            if children_map[course]:
                for child in children_map[course]:
                    if in_degree_map[child] - 1 == 0:
                        q.append(child)
                    in_degree_map[child] -= 1
        
        return count == numCourses



        