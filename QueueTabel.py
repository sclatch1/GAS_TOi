#Queue tabel linked based
#from arraybased_queue import MyQueue
from MyQueue import MyQueue

class QueueTabel:
    def __init__(self):
        self.myQueue = MyQueue()

    def isEmpty(self):
        self.myQueue.isEmpty()

    def enqueu(self,item):
        self.myQueue.enqueue(item)

    def getFront(self):
        self.myQueue.getFront()

    def save(self):
        self.myQueue.save()

    def load(self,list):
        self.myQueue.load(list)


