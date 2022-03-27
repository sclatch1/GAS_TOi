#============================================================================
# Name        : arraybased_queue.py
# Author      : Daan Thielemans
# Version     : 1.0
# Copyright   : GAS - BA1 Informatica - Daan Thielemans - University of Antwerp
# Description : Arraybased queue implementation in python
#============================================================================

class MyQueue():
    def __init__(self, max_size):
        self.a = [None] * max_size
        self.max_size=max_size

    def isEmpty(self):
        for i in self.a:
            if (i != None):
                return False
        return True

    def enqueue(self, item):
        if self.a[self.max_size-1] != None:
            return False
        x = self.max_size-1
        for i in self.a[::-1]:
            if x != self.max_size-1:
                self.a[x+1] = i
            x -= 1
        self.a[0] = item
        return True

    def dequeue(self):
        x = self.max_size-1
        for i in self.a[::-1]:
            if (i != None):
                self.a[x] = None
                return [i, True]
            x -= 1
        return [None, False]

    def getFront(self):
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