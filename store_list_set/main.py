import collections
import random


class Store:
    def __init__(self):
        self.values = []
        self.map = {}

    def insert(self, value):
        if value in self.map:
            return 
        
        self.values.append(value)
        self.map[value] = len(self.values) - 1
        print(self.map)
        print(self.values)

    def remove(self, value):
        if value not in self.map:
            return
        
        index = self.map[value]
        last_val = self.values[-1]
        self.values[-1] = value
        self.map[last_val] = index
        
        self.values[index] = last_val

        self.values.pop()
        del self.map[value]
        print(self.map)
        print(self.values)

    def get_random(self):
        return random.choice(self.values)
    
class NonUniqueStore:
    def __init__(self):
        self.values = []
        self.map = collections.defaultdict(set)

    def insert(self, value):
        self.values.append(value)
        self.map[value].add(len(self.values)-1)
        print(self.map)
        print(self.values)

    def remove(self, value):
        if value not in self.map:
            return
        
        index = next(iter(self.map[value]))
        
        # swapping
        last_val = self.values[-1]
        self.values[-1] = value
        self.values[index] = last_val
        self.map[last_val].add(index)

        self.values.pop()
        self.map[value].pop()
        print(self.map)
        print(self.values)

    def get_random(self):
        return random.choice(self.values)
    
if __name__ == "__main__":
    s = NonUniqueStore()
    s.insert(3)
    s.insert(4)
    s.insert(4)
    s.insert(5)
    s.remove(3)
    s.remove(4)
    print(s.get_random())