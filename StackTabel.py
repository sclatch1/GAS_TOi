#============================================================================
# Name        : StackTabel.py
# Author      : David Scalais
# Copyright   : GAS - BA1 Informatica - David Scalais - University of Antwerp
# Description : array-based StackTabel implementation in python
#============================================================================
from arraybased_stack import MyStack

class StackTabel:
    def __init__(self,max_size):
        self.stack = MyStack(max_size)

    def TabelIsEmpty(self):
        self.stack.isEmpty()

    def TabelPush(self,newItem):
        self.stack.push(newItem)

    def TabelPop(self):
        self.stack.pop()

    def TabelSave(self):
        self.stack.save()

    def TabelLoad(self,list):
        self.stack.load(list)
