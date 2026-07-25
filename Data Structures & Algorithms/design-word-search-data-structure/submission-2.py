class WordDictionary:

    def __init__(self):
        self.root = CharNode()

    def addWord(self, word: str) -> None:
        if word[0] not in self.root.children:
            self.root.children[word[0]] = CharNode()
        
        curr = self.root.children[word[0]]
        
        for i in range(1, (len(word))):
            if word[i] not in curr.children:
                curr.children[word[i]] = CharNode()
            
            curr = curr.children[word[i]]
        
        curr.is_word = True


    def search(self, word: str) -> bool:
        if word[0] != "." and word[0] not in self.root.children:
            return False

        def _dfs(node, i):
            if i == len(word):
                return node.is_word
            
            if word[i] != ".":
                if word[i] in node.children:
                    return _dfs(node.children[word[i]], i+1)
                else:
                    return False
            else:

                for char in node.children:
                    result = _dfs(node.children[char], i+1)
                    if result:
                        return True

                return False

        return _dfs(self.root, 0)



        
class CharNode:
    
    def __init__(self):
        self.children = {}
        self.is_word = False