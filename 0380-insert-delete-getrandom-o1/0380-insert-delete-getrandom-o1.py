class RandomizedSet:

    def __init__(self):
        self.random_object = set()
        

    def insert(self, val: int) -> bool:
        if val not in self.random_object:
            self.random_object.add(val)
            return True
        else:
            return False
            
        

    def remove(self, val: int) -> bool:
        if val in self.random_object:
            self.random_object.remove(val)
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        return random.choice(tuple(self.random_object))
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()