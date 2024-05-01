class MyEnumerate:
    def __init__(self, seq):
        self.pos = 0
        self.seq = seq
    def __iter__(self):
        return self
    def __next__(self):
        if self.pos >= len(self.seq):
            raise StopIteration
        else:
            self.pos += 1
            return (self.pos-1)*100, self.seq[self.pos-1]
        
for index, letter in MyEnumerate('abc'):
    print(f"{index} : {letter}")
    
