class Block:
    def __init__(self, q):
        self.width = q[0]
        self.length = q[1]
        self.height = q[2]
        
    def get_width(self):
        return self.width
        
    def get_length(self):
        return self.length
        
    def get_height(self):
        return self.height 
        
    def get_volume(self):
        return self.width * self.height * self.length
        
    def get_surface_area(self):
        return (self.width * self.height + self.height * self.length + self.width * self.length) * 2
    
b = Block([2,4,6])
print(b.get_width())
print(b.get_length())
print(b.get_height())
print(b.get_volume())
print(b.get_surface_area())