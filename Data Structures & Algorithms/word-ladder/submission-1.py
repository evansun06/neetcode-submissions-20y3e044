from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        WORD_SIZE = len(beginWord)

        def buildGraph() -> dict:
            nonlocal WORD_SIZE
            # returns an adjacency list of possible traversal options
            graph = defaultdict(list)

            for word in wordList:
                for i in range(WORD_SIZE):
                    # exclude index i 
                    start = word[:i]
                    end = word[i + 1:]

                    hash = start + "*" + end
                    graph[hash].append(word)
            
            return graph
        
        graph = buildGraph()
        queue = deque([beginWord])
        visited = set()
        distance = 1

        while queue:
            
            for _ in range(len(queue)):
                word = queue.popleft()

                if word == endWord:
                    return distance

                for i in range(WORD_SIZE):
                    # exclude index i 
                    start = word[:i]
                    end = word[i + 1:]

                    hash = start + "*" + end

                    
                    
                    for possible in graph[hash]:
                        if possible in visited:
                            continue
                        
                        queue.append(possible)
                        visited.add(possible)

            distance += 1
                    
        return 0

         


