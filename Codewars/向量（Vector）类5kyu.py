import operator

class Vector:
    def __init__(self, collection):
        self.collection = collection
        
    def __str__(self):
        return '(' + ','.join(str(i) for i in self.collection) + ')'
    
    def equals(self, other):
        return operator.eq(self.collection, other.collection)
    
    def add(self, f = None):
        if len(self.collection) == len(f.collection):
            i = []
            for j in self.collection:
                i.append(j)
            for l in range(len(self.collection)):
                i[l] = self.collection[l] + f.collection[l]
            return Vector(i)
        raise IndexError()
        
    def subtract(self, f):
        if len(self.collection) == len(f.collection):
            i = []
            for j in self.collection:
                i.append(j)
            for l in range(len(self.collection)):
                i[l] = self.collection[l] - f.collection[l]
            return Vector(i)
        raise IndexError()
            
    def dot(self, f):
        if len(self.collection) == len(f.collection):
            sums = 0
            i = []
            for j in self.collection:
                i.append(j)
            for l in range(len(self.collection)):
                i[l] = self.collection[l] * f.collection[l]
                sums += i[l]
            return sums
        raise IndexError()
        
    def norm(self):
        sums = 0
        i = []
        for j in self.collection:
            i.append(j)    
        for l in range(len(self.collection)):
            i[l] **= 2
            sums += i[l]
        return sums ** 0.5
                
                

a = Vector([1, 2, 3])
b = Vector([3, 4, 5])
print(a.add(b))
print(a.subtract(b))
print(a.dot(b))
print(a.norm())