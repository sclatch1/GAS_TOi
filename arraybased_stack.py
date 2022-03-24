#============================================================================
# Name        : arraybased_stack.py
# Author      : Daan Thielemans
# Version     : 1.0
# Copyright   : GAS - BA1 Informatica - Daan Thielemans - University of Antwerp
# Description : Arraybased stack implementation in python
#============================================================================

class MyStack():
    def __init__(self, max_size):
        self.a = [None] * max_size
        self.max_size=max_size

    def isEmpty(self):
        for i in self.a:
            if (i != None):
                return False
        return True

    def push(self, item):
        x = 0
        for i in self.a:
            if (i == None):
                self.a[x] = item
                return True
            x += 1
        return False

    def pop(self):
        x = self.max_size-1
        for i in self.a[::-1]:
            if (i != None):
                self.a[x] = None
                return [i, True]
            x -= 1
        return [None, False]

    def getTop(self):
        for i in self.a[::-1]:
            if (i != None):
                return [i, True]
        return [None, False]

    def save(self):
        out = []
        for i in self.a:
            if i is not None:
                out.append(i)
        return out

    def load(self, list):
        self.a=list
        self.max_size=len(list)


s = MyStack(2)
print(s.isEmpty())
print(s.getTop())
print(s.pop())
print(s.push(2))
print(s.push(4))
print(s.push(1))
print(s.isEmpty())
print(s.pop())
s.push(5)
print(s.save())

s.load(['a','b','c'])
print(s.save())
print(s.pop())
print(s.save())
print(s.getTop())
print(s.save())
