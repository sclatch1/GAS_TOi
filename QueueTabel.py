#Queue tabel linked based

#============================================================================
# Name        : QueueTabel.py
# Author      : David Scalais
# Copyright   : GAS - BA1 Informatica - David Scalais - University of Antwerp
# Description : link-based QueueTabel implementation in python
#============================================================================


from MyQueue import MyQueue

class QueueTabel:
    def __init__(self):
        self.myQueue = MyQueue()

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


