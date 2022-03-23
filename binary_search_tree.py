#============================================================================
# Name        : binary_search_tree.py
# Author      : Daan Thielemans
# Version     : 1.0
# Copyright   : GAS - BA1 Informatica - Daan Thielemans - University of Antwerp
# Description : Binary search tree implementation in python
#============================================================================

class BST:
    def __init__(self):                             #create
        self.root = None
        self.pointer = None
        self.size = 0

    def isEmpty(self):                              #isEmpty
        if self.size==0:
            return True
        return False

    def getSize(self):                              #getSize
        return self.size

    def searchTreeInsert(self, item):                  #insert
        key = item[0]
        inhoud = item[1]
        self.pointer = self.root
        if self.size == 0:
            self.root=Node_tree(key, None, None, None, None, inhoud)
            self.pointer=self.root
            self.size+=1
            self.pointer = self.root
            self.pointer.child = 1
            return True
        parent = self.root
        while (True):
            if key < self.pointer.key:
                parent = self.pointer
                self.pointer=self.pointer.child1
                if self.pointer==None:
                    parent.child1=Node_tree(key, parent, 1, None, None, inhoud)
                    self.size+=1
                    self.pointer = self.root
                    return True
            elif key > self.pointer.key:
                parent = self.pointer
                self.pointer=self.pointer.child2
                if self.pointer==None:
                    parent.child2=Node_tree(key, parent, 2, None, None, inhoud)
                    self.size+=1
                    self.pointer = self.root
                    return True

    def searchTreeDelete(self, key):
        self.pointer = self.root
        while (self.pointer.key != key):
            if self.pointer == None:
                return False
            if key<self.pointer.key:
                self.pointer=self.pointer.child1
            if self.pointer == None:
                return False
            if key>self.pointer.key:
                self.pointer=self.pointer.child2
        # if leaf
        if self.pointer.child1==None and self.pointer.child2==None:
            if self.pointer.child == 1:
                self.pointer.parent.child1 = None
            if self.pointer.child == 2:
                self.pointer.parent.child2 = None
            return True
        # if 1 child
        if self.pointer.child1 != None and self.pointer.child2 == None:
            if self.pointer.child == 1:
                self.pointer.child2.parent = self.pointer.parent
                self.pointer.parent.child1 = self.pointer.child1
                self.pointer.child1.child = 1
            if self.pointer.child == 2:
                self.pointer.child1.parent = self.pointer.parent
                self.pointer.parent.child2 = self.pointer.child1
                self.pointer.child1.child = 2
            return True
        if self.pointer.child1 == None and self.pointer.child2 != None:
            if self.pointer.child == 1:
                self.pointer.child2.parent = self.pointer.parent
                self.pointer.parent.child1 = self.pointer.child2
                self.pointer.child2.child = 1
            if self.pointer.child == 2:
                self.pointer.child1.parent = self.pointer.parent
                self.pointer.parent.child2 = self.pointer.child2
                self.pointer.child2.child = 2
            return True
        # if 2 children
        if self.pointer.child1 != None and self.pointer.child2 != None:
            self.pointer=self.pointer.child2
            while (self.pointer.child1 != None):
                self.pointer = self.pointer.child1
            temporary_pointer=self.pointer
            while (self.pointer.key != key):
                self.pointer = self.pointer.parent
            self.pointer.key= temporary_pointer.key
            self.pointer.inhoud = temporary_pointer.inhoud
            self.pointer = self.pointer.child2
            if(self.pointer.child1 != None):
                while (self.pointer.child1.child1 != None):
                    self.pointer = self.pointer.child1
                self.pointer.child1=None
            else:
                self.pointer.parent.child2=None
        self.size -= 1
        self.pointer = self.root
        return True

    def searchTreeRetrieve(self, key):
        self.pointer = self.root
        while (self.pointer.key != key):
            if key < self.pointer.key:
                self.pointer = self.pointer.child1
            elif key > self.pointer.key:
                self.pointer = self.pointer.child2
        return [self.pointer.inhoud, True]

    def inorderTraverse(self, functioncall=None):
        self.pointer = self.root
        output = []
        if self.pointer.child1 != None:
            self.pointer=self.pointer.child1
            output += (inorderTraverse(self.pointer))
            self.pointer = self.pointer.parent
        output.append(self.pointer.inhoud)
        if self.pointer.child2 != None:
            self.pointer=self.pointer.child2
            output += (inorderTraverse(self.pointer))
            self.pointer = self.pointer.parent
        if functioncall==print:
            for i in output:
                print(i)
        return(output)

    def save(self):
        self.pointer = self.root
        output = {'root': self.pointer.key}
        if self.pointer.child1 != None or self.pointer.child2 != None:
            output['children'] = []
            if self.pointer.child1 != None:
                self.pointer = self.pointer.child1
                output['children'].append(save(self.pointer))
                self.pointer = self.pointer.parent
            else:
                output['children'].append(None)
            if self.pointer.child2 != None:
                self.pointer = self.pointer.child2
                output['children'].append(save(self.pointer))
                self.pointer = self.pointer.parent
            else:
                output['children'].append(None)
        return output

    def load(self, dict):
        self.root = None
        self.pointer = None
        self.size = 0
        dict_list = dict_to_list(dict)
        for i in dict_list:
            self.searchTreeInsert([i,i])
        return True

def dict_to_list(dict):
    out = []
    keys = dict.keys()
    for i in keys:
        if i == 'root':
            out.append(dict['root'])
        if i == 'children':
            for j in dict['children']:
                if j is not None:
                    out += (dict_to_list(j))
    return out

def inorderTraverse(pointer):
    output = []
    if pointer.child1 != None:
        pointer=pointer.child1
        output += (inorderTraverse(pointer))
        pointer = pointer.parent
    output.append(pointer.inhoud)
    if pointer.child2 != None:
        pointer=pointer.child2
        output += (inorderTraverse(pointer))
        spointer = pointer.parent
    return(output)

def save(pointer):
    output = {'root': pointer.key}
    if pointer.child1 != None or pointer.child2 != None:
        output['children'] = []
        if pointer.child1 != None:
            pointer = pointer.child1
            output['children'].append(save(pointer))
            pointer = pointer.parent
        else:
            output['children'].append(None)
        if pointer.child2 != None:
            pointer = pointer.child2
            output['children'].append(save(pointer))
            pointer = pointer.parent
        else:
            output['children'].append(None)
    return output


class Node_tree:
    def __init__(self, key, parent, child, child1, child2, inhoud = None):
        self.key = key
        self.inhoud = inhoud
        self.parent = parent
        self.child = child
        self.child1 = child1
        self.child2 = child2

def createTreeItem(a, b):
    return [a, b]

"""
t = BST()
t.load({'root': 100, 'children': [{'root': 50, 'children': [{'root': 20}, {'root': 90, 'children': [{'root': 70}, None]}]}, {'root': 200, 'children': [{'root': 120}, {'root': 210}]}]})
print(t.save())
t.searchTreeDelete(90)
print(t.save())
t.searchTreeDelete(70)
print(t.save())
t.searchTreeDelete(100)
print(t.save())
"""