#Queue tabel linked based

#============================================================================
# Name        : QueueTabel.py
# Author      : David Scalais
# Copyright   : GAS - BA1 Informatica - David Scalais - University of Antwerp
# Description : array-based QueueTabel implementation in python
#============================================================================


from arraybased_queue import MyQueue

class QueueTabel:
    def __init__(self,max_size):
        self.myQueue = MyQueue(max_size)

    def TableIsEmpty(self):
        self.myQueue.isEmpty()

    def TableEnqueu(self,item):
        self.myQueue.enqueue(item)

    def TableGetFront(self):
        self.myQueue.getFront()

    def TableSave(self):
        self.myQueue.save()

    def TableLoad(self,list):
        self.myQueue.load(list)

