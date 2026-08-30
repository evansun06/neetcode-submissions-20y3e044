from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
            nodes = wordList

            edges = wildcard a single character in the word
                - bat -> *at, b*t, ba*

            preprocessing: make an adjcenecy list O(len(wordList) * max(len(word) in wordList))

        """

        adjc_list = defaultdict(list)


        for word in wordList:
            for i in range(len(word)):
                key = word[:i] + "*" + word[i + 1:]
                adjc_list[key].append(word)
        
        visited = set([beginWord])
        q = deque()
        q.append(beginWord)
        distance = 1

        while q:
            for _ in range(len(q)):
                curr_word = q.popleft()

                if curr_word == endWord:
                    return distance
                
                for i in range(len(curr_word)):
                    key = curr_word[:i] + "*" + curr_word[i + 1:]
                    
                    for next_word in adjc_list[key]:
                        if next_word not in visited:
                            q.append(next_word)
                            visited.add(next_word)

            distance += 1
        
        return 0


