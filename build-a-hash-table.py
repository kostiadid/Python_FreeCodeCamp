class HashTable:
    def __init__(self):
        self.collection = {}
    def hash(self, el):
        summury = 0
        for i in el:
            summury += ord(i)
        return summury
    def add(self,key,value):
        h = self.hash(key)
        if h not in self.collection:
            self.collection[h] = {}
        self.collection[h][key] = value

    def remove(self,key):
        h = self.hash(key)
        if h in self.collection:
            del self.collection[h][key]
                   
    def lookup(self,key):
        h = self.hash(key)
        if not  h in self.collection:
            return None
        return  self.collection[h][key]
