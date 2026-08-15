import random

class RandomizedSet:

    def __init__(self):
        self.map = {}
        self.array = []

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        else:
            self.array.append(val)
            self.map[val] = len(self.array) - 1
            return True


    def remove(self, val: int) -> bool:
        if val in self.map:
            index = self.map[val]
            end = self.array[-1]
            self.array[index] = end
            self.map[end] = index
            self.array.pop()
            self.map.pop(val)
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        ran = random.randint(0, len(self.array) - 1)
        return self.array[ran]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()