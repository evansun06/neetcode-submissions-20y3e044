class PrefixTree:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        curr = self.root
        for i in range(len(word)):
            if word[i] in curr:
                curr = curr[word[i]]
            else:
                curr[word[i]] = {}
                curr = curr[word[i]]
        curr["*"] = True



    def search(self, word: str) -> bool:
        curr = self.root
        for i in range(len(word)):
            if word[i] in curr:
                curr = curr[word[i]]
            else:
                return False
        return True if "*" in curr else False
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for i in range(len(prefix)):
            if prefix[i] in curr:
                curr = curr[prefix[i]]
            else:
                return False
        return True
        
        