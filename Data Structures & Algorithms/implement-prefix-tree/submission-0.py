class PrefixTree:

    def __init__(self):
        self.letters = [None] * 26
        
    def insert(self, word: str) -> None:
        if self.letters[ord(word[0]) - 97] is None:
            self.letters[ord(word[0]) - 97] = TreeNode(word[0])
        
        root =  self.letters[ord(word[0]) - 97]

        def _insert(node: TreeNode):
            curr = node
            for i in range(1, len(word)):
                if not curr.children[ord(word[i]) - 97]:
                    curr.children[ord(word[i]) - 97] = TreeNode(word[i])

                curr = curr.children[ord(word[i]) - 97]
                
            curr.is_word = True
        _insert(root)

    def _search(self, node: TreeNode, word):
        curr = node
        for i in range(1, len(word)):
            if not curr.children[ord(word[i]) - 97]:
                return False, None

            curr = curr.children[ord(word[i]) - 97]

        return True, curr

    def search(self, word: str) -> bool:
        if self.letters[ord(word[0]) - 97] is None:
            return False
        
        root =  self.letters[ord(word[0]) - 97]

        result, curr = self._search(root, word)

        return result and curr.is_word

    def startsWith(self, prefix: str) -> bool:
        if self.letters[ord(prefix[0]) - 97] is None:
            return False
        
        root =  self.letters[ord(prefix[0]) - 97]
        result, _ = self._search(root, prefix)
    
        return result


class TreeNode:

    def __init__(self, char):
        self.char = char
        self.children = [None] * 26
        self.is_word = False
    
