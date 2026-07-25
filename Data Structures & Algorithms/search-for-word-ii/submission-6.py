class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
    
        # trie = PrefixTree(words)
        trie = PrefixTree(words)
        result = []
        
        def dfs(curr: tuple, path: list[tuple], node):

            if curr in path or out_of_bounds(curr):
                return
            
            path.append(curr)
            char = board[curr[0]][curr[1]]
            if char in node.children:
                if node.children[char].is_word:
                    result.append(to_word(path))
                    node.children[char].is_word = False

                dfs((curr[0] + 1, curr[1]), path, node.children[char])
                dfs((curr[0], curr[1] + 1), path, node.children[char])
                dfs((curr[0] - 1, curr[1]), path, node.children[char])
                dfs((curr[0], curr[1] - 1), path, node.children[char])

            path.pop()
        
        def to_word(path: list[tuple]) -> str:
            return "".join([board[t[0]][t[1]] for t in path])
        
        def out_of_bounds(curr: tuple) -> bool:
            return (curr[0] < 0 or curr[0] >= len(board)) or (curr[1] < 0 or curr[1] >= len(board[0]))
        
        for x in range(len(board)):
            for y in range(len(board[0])):
                dfs((x, y), [], trie.root)
        
        return result
    

class PrefixTree:
    
    def __init__(self, words):
        self.root = PrefixNode()

        for word in words:
            self.insert(word)

    def insert(self, word: str):
          
        curr = self.root

        for i in range(0, len(word)):
            if word[i] not in curr.children:
                curr.children[word[i]] = PrefixNode()

            curr = curr.children[word[i]]
        
        curr.is_word = True
        curr.word = word

class PrefixNode:

    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = None
    
