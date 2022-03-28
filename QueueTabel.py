#Queue tabel linked based

#============================================================================
# Name        : QueueTabel.py
# Author      : David Scalais
# Copyright   : GAS - BA1 Informatica - David Scalais - University of Antwerp
# Description : array-based QueueTabel implementation in python
#============================================================================


from MyQueue import MyQueue


class QueueTabel:
    def __init__(self):
        self.myQueue = MyQueue()

    def IsEmpty(self):
        return self.myQueue.isEmpty()

    def enqueue(self,item):
        self.myQueue.enqueue(item)

    def dequeue(self):
        return self.myQueue.dequeue()

    def GetFront(self):
        return self.myQueue.getFront()

    def save(self):
        return self.myQueue.save()

    def load(self,list):
        self.myQueue.load(list)


