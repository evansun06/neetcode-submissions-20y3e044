class MyHashSet:

    def __init__(self):
        self.buckets = [None] * 10
        self.size = 0

    def add(self, key: int) -> None:
        # size/buckets >= 0.75
        if self.size >= 0.75 * len(self.buckets):
            self._resizeUp()

        hashed_key = self._hash(key)

        if self.buckets[hashed_key] is None:
            self.buckets[hashed_key] = [key]
        else:
            if key not in self.buckets[hashed_key]:
                self.buckets[hashed_key].append(key)
                self.size += 1

    def remove(self, key: int) -> None:
        hashed_key = self._hash(key)

        if self.buckets[hashed_key] is not None and key in self.buckets[hashed_key]:
            self.buckets[hashed_key].remove(key)
            self.size -= 1

    def contains(self, key: int) -> bool:
        hashed_key = self._hash(key)

        if self.buckets[hashed_key] is None or key not in self.buckets[hashed_key]:
            return False
        else:
            return True

    
    def _hash(self, key: int) -> int:
        return key % len(self.buckets)
    
    def _resizeUp(self):
        old_buckets = self.buckets
        self.buckets = [None] * (len(old_buckets) * 2)

        for bucket in old_buckets:
            if bucket is None:
                continue
            for key in bucket:
                hashed_key = self._hash(key)
                if self.buckets[hashed_key] is None:
                    self.buckets[hashed_key] = [key]
                else:
                    self.buckets[hashed_key].append(key)


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)