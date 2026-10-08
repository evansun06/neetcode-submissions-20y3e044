from collections import defaultdict, deque

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        """
        ["hrn","hrf","er","enn","rfnn"]

        n < f
        h < e
        h < r
        r < n
        e < r

        inorder:
        h - 0
        r - 2
        n - 1
        e - 1
        f - 1

        adjc_list:
        h [e, r]
        n [f]
        r [n]
        e [r]

        hernf
        """

        adjc_list = defaultdict(set)
        inorders = {char: 0 for word in words for char in word}

        for less, greater in zip(words, words[1:]):
            if len(less) > len(greater) and less.startswith(greater):
                return ""

            for a, b in zip(less, greater):
                if a != b:
                    if b not in adjc_list[a]:
                        adjc_list[a].add(b)
                        inorders[b] += 1
                    break

        q = deque()
        visited = set()

        for char in inorders:
            if inorders[char] == 0:
                q.append(char)
                visited.add(char)

        res = []
        while q:
            char = q.popleft()
            res.append(char)

            for adjc_char in adjc_list[char]:

                inorders[adjc_char] -= 1
                if inorders[adjc_char] == 0:
                    q.append(adjc_char)

        return "".join(res) if len(res) == len(inorders) else ""
    


        