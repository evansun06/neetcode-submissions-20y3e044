import random

class RandomizedSet:

    def __init__(self):
        self.hash_set = set()

    def insert(self, val: int) -> bool:
        return self.hash_set.add(val)

    def remove(self, val: int) -> bool:
        if val in self.hash_set:
            self.hash_set.remove(val)
            return True
        
        return False

    def getRandom(self) -> int:
        ran = random.randint(0, len(self.hash_set) - 1)
        return list(self.hash_set)[ran]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()