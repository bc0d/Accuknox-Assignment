class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
    
    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}

#function calling
rect = Rectangle(4, 6)

#iteration
for i in rect:
    print(i)