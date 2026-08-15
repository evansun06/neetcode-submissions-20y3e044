class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        class graph:
            from collections import defaultdict, deque

            # define graph = (V, E)
            # where nodes v = variables 
            # where edges e = represents the multiplier required to relate one variable to another

            # representation
            # adjacency list
            # maps node -> edge (var, multiplier)

            def __init__(self, equations, values):

                self.adjlist = defaultdict(list)

                for i in range(len(equations)):
                    # numerator
                    self.adjlist[equations[i][0]].append((equations[i][1], values[i]))
        
                    # denominator
                    self.adjlist[equations[i][1]].append((equations[i][0], 1.0 / values[i]))

            def query(self, equation) -> float:

                q = deque()
                visited = set()

                q.append((equation[0], 1.0))
                visited.add(equation[0])

                if (equation[0] not in self.adjlist 
                or equation[1] not in self.adjlist
                ):
                    return -1.0

                while q:
                    node, multiplier = q.popleft()
                    
                    if node == equation[1]:
                        return multiplier

                    for adj in self.adjlist[node]:

                        if adj[0] not in visited:
                            visited.add(adj[0])
                            q.append((adj[0], multiplier * adj[1]))
                
                return -1.0


            
        graph = graph(equations, values)
        print(graph.adjlist)
        result = []
        for q in queries:
            result.append(float(graph.query(q)))
        
        return result

        
        

        