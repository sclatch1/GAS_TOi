#============================================================================
# Name        : Two_Tree_Four_Tree.py
# Author      : Daan Thielemans
# Version     : 1.0
# Copyright   : GAS - BA1 Informatica - Daan Thielemans - University of Antwerp
# Description : 2-3-4 tree implementation in python
#============================================================================

def createTreeItem(key,val):
    return [key, val]

class TwoThreeFourTree:
    def __init__(self):
        self.root = None
        self.pointer = None
        self.size = 0

    def isEmpty(self):
        if self.size==0:
            return True
        return False

    def getSize(self):
        return self.size

    def insertItem(self, treeitem):
        key = treeitem[0]
        value = treeitem[1]
        self.pointer = self.root
        # if first node
        if self.size == 0:
            self.root = Node(key, value)
            self.size += 1
            return True
        # if not first node
        if self.pointer.type == 4:  # if a 4-node, split
            self.split(self.pointer)
            self.pointer = self.pointer.parent
        while (self.pointer.children_count != 0):         # go to leaf
            if self.pointer.type == 4:                    # if a 4-node, split
                self.split(self.pointer)
                self.pointer = self.pointer.parent
            elif key < self.pointer.keys[0]:              # if smaller than first value, go left
                self.pointer = self.pointer.children[0]
            elif self.pointer.items[1] != None:           # if bigger than second value, go right
                if key > self.pointer.keys[1]:
                    self.pointer = self.pointer.children[2]
                else:  # else, go middle
                    self.pointer = self.pointer.children[1]
            else:                                         # else, go middle
                self.pointer = self.pointer.children[1]
            if self.pointer.type == 4:                    # if a 4-node, split
                self.split(self.pointer)
                self.pointer = self.pointer.parent
        if key < self.pointer.keys[0]:
            self.pointer.keys[2] = self.pointer.keys[1]
            self.pointer.keys[1] = self.pointer.keys[0]
            self.pointer.keys[0] = key
            self.pointer.items[2] = self.pointer.items[1]
            self.pointer.items[1] = self.pointer.items[0]
            self.pointer.items[0] = value
        elif self.pointer.keys[1] == None or key < self.pointer.keys[1]:
            self.pointer.keys[2] = self.pointer.keys[1]
            self.pointer.keys[1] = key
            self.pointer.items[2] = self.pointer.items[1]
            self.pointer.items[1] = value
        elif self.pointer.keys[2] == None or key < self.pointer.keys[2]:
            self.pointer.keys[2] = key
            self.pointer.items[2] = value
        self.pointer.type += 1
        self.size += 1
        return True

    def deleteItem(self, key):
        self.pointer = self.root
        if self.inorderTraverse().count(key) == 0:
            return False
        while (self.pointer.keys.count(key) == 0):  # go to item
            if self.pointer.type == 2:  # if a 2-node, merge
                self.merge(self.pointer)
                self.pointer = self.pointer.parent
            if key < self.pointer.keys[0]:  # if smaller than first value, go left
                self.pointer = self.pointer.children[0]
            if key > self.pointer.keys[1]:
                if self.pointer.type == 4:
                    if key > self.pointer.keys[2]:  # if bigger than last value, go right
                        self.pointer = self.pointer.children[3]
                    else:  # if bigger than second value, go right
                        self.pointer = self.pointer.children[2]
                else:
                    self.pointer = self.pointer.children[2]
            else:  # else, go middle
                self.pointer = self.pointer.children[1]
        if self.pointer.children_count == 0:            # if leaf
            i = 0
            while (i < 3):
                if self.pointer.keys[i] != key:
                    i += 1
                else:
                    break
            while (i < 3):
                self.pointer.keys[i] = self.pointer.keys[i + 1]
                self.pointer.items[i] = self.pointer.items[i + 1]
                i += 1
            self.pointer.keys[2] = None
            self.pointer.items[2] = None
            self.pointer.type -= 1
            self.size -= 1
            return True
        else:
            pointer = self.pointer
            while (pointer.children_count != 0):  # go to inorder sucessor (leaf)
                if pointer == self.pointer:
                    pointer = self.pointer.children[1]
                elif pointer.type == 2:  # if a 2-node, merge
                    self.merge(pointer)
                    pointer = pointer.parent
                else:
                    pointer = pointer.children[0]
                if pointer.type == 2:  # if a 2-node, merge
                    self.merge(pointer)
                    pointer = pointer.parent
            i = 0
            while (i < 3):
                if self.pointer.keys[i] != key:
                    i += 1
                else:
                    break
            self.pointer.keys[i] = pointer.keys[0]
            self.pointer.items[i] = pointer.items[0]
            pointer.keys[0] = pointer.keys[1]
            pointer.keys[1] = pointer.keys[2]
            pointer.keys[2] = None
            pointer.items[0] = pointer.items[1]
            pointer.items[1] = pointer.items[2]
            pointer.items[2] = None
            pointer.type -= 1
            self.size -= 1
            return True

    def merge(self, pointer):
        # 1. Als de ouder en sibling van de om te vormen knoop 2-knopen zijn
        if pointer.parent.type == 2 and pointer.parent.children[0].type == 2 and pointer.parent.children[1].type == 2:
            pointer = pointer.parent
            index = 0
            while index < 4:
                if pointer.parent.children[index] == pointer:
                    pointer.parent.children[index] = Node(pointer.children[0].keys[0], pointer.children[0].items[0], pointer.parent)
                    break
                index += 1
            pointer.parent.children[index].keys[1] = pointer.keys[0]
            pointer.parent.children[index].items[1] = pointer.items[0]
            pointer.parent.children[index].keys[2] = pointer.children[1].keys[0]
            pointer.parent.children[index].items[2] = pointer.children[1].items[0]
            pointer.parent.children[index].children[0] = pointer.children[0].children[0]
            pointer.parent.children[index].children[1] = pointer.children[0].children[1]
            pointer.parent.children[index].children[3] = pointer.children[1].children[0]
            pointer.parent.children[index].children[4] = pointer.children[1].children[1]
            pointer.children[0].children[0].parent = pointer.parent.children[index]
            pointer.children[0].children[1].parent = pointer.parent.children[index]
            pointer.children[1].children[0].parent = pointer.parent.children[index]
            pointer.children[1].children[1].parent = pointer.parent.children[index]
            pointer.parent.children[index].type = 4
            pointer.parent.children[index].children_count = 4
        # 2. Als de ouder van de om te vormen knoop een 3-knoop is
        elif pointer.parent.type == 3:
            if pointer.parent.children[0].type == 2 and pointer.parent.children[1].type == 2:
                pointer = pointer.parent
                index = 0
                while index < 4:
                    if pointer.parent.children[index] == pointer:
                        break
                    index += 1
                pointer.parent.children[index] = Node(pointer.keys[1], pointer.items[1],pointer.parent)
                pointer.parent.children[index].children[1] = pointer.children[2]
                pointer.children[2].parent = pointer.parent.children[index]
                pointer.parent.children[index].children[0] = Node(pointer.children[0].keys[0], pointer.children[0].items[0],pointer.parent.children[index])
                pointer.parent.children[index].children[0].keys[1] = pointer.keys[0]
                pointer.parent.children[index].children[0].items[1] = pointer.items[0]
                pointer.parent.children[index].children[0].keys[2] = pointer.children[1].keys[0]
                pointer.parent.children[index].children[0].items[2] = pointer.children[1].items[0]
                pointer.parent.children[index].children[0].children[0] = pointer.children[0].children[0]
                pointer.parent.children[index].children[0].children[1] = pointer.children[0].children[1]
                pointer.parent.children[index].children[0].children[2] = pointer.children[1].children[0]
                pointer.parent.children[index].children[0].children[3] = pointer.children[1].children[1]
                pointer.children[0].children[0].parent =  pointer.parent.children[index].children[0]
                pointer.children[0].children[1].parent = pointer.parent.children[index].children[0]
                pointer.children[1].children[0].parent = pointer.parent.children[index].children[0]
                pointer.children[1].children[1].parent = pointer.parent.children[index].children[0]
                pointer.parent.children[index].children[0].type = 4
                pointer.parent.children[index].children[0].children_count = 4
            elif pointer.parent.children[2].type == 2 and pointer.parent.children[1].type == 2:
                pointer = pointer.parent
                index = 0
                while index < 4:
                    if pointer.parent.children[index] == pointer:
                        break
                    index += 1
                pointer.parent.children[index] = Node(pointer.keys[0], pointer.items[0], pointer.parent)
                pointer.parent.children[index].children[0] = pointer.children[0]
                pointer.children[0].parent = pointer.parent.children[index]
                pointer.parent.children[index].children[1] = Node(pointer.children[1].keys[0],pointer.children[1].items[0],pointer.parent.children[index])
                pointer.parent.children[index].children[1].keys[1] = pointer.keys[1]
                pointer.parent.children[index].children[1].items[1] = pointer.items[1]
                pointer.parent.children[index].children[1].keys[2] = pointer.children[2].keys[0]
                pointer.parent.children[index].children[1].items[2] = pointer.children[2].items[0]
                pointer.parent.children[index].children[1].children[0] = pointer.children[1].children[0]
                pointer.parent.children[index].children[1].children[1] = pointer.children[1].children[1]
                pointer.parent.children[index].children[1].children[2] = pointer.children[2].children[0]
                pointer.parent.children[index].children[1].children[3] = pointer.children[2].children[1]
                pointer.children[1].children[0].parent = pointer.parent.children[index].children[1]
                pointer.children[1].children[1].parent = pointer.parent.children[index].children[1]
                pointer.children[2].children[0].parent = pointer.parent.children[index].children[1]
                pointer.children[2].children[1].parent = pointer.parent.children[index].children[1]
                pointer.parent.children[index].children[1].type = 4
                pointer.parent.children[index].children[1].children_count = 4
            else:
                return False
        # 3. Als de ouder van de om te vormen knoop een 4-knoop is
        elif pointer.parent.type == 4:
            if pointer.parent.children[0].type == 2 and pointer.parent.children[1].type == 2:
                pointer = pointer.parent
                pointer.children[0].keys[2] = pointer.children[1].keys[0]
                pointer.children[0].items[2] = pointer.children[1].items[0]
                pointer.children[0].keys[1] = pointer.keys[0]
                pointer.children[0].items[1] = pointer.items[0]
                pointer.children[0].children[2] = pointer.children[1].children[0]
                pointer.children[0].children[3] = pointer.children[1].children[1]
                pointer.children[0].children[2].parent = pointer.children[0]
                pointer.children[0].children[3].parent = pointer.children[0]
                pointer.children[1] = pointer.children[2]
                pointer.children[2] = pointer.children[3]
                pointer.children[3] = None
                pointer.keys[0] = pointer.keys[1]
                pointer.items[0] = pointer.items[1]
                pointer.keys[1] = pointer.keys[2]
                pointer.items[1] = pointer.items[2]
                pointer.keys[2] = None
                pointer.items[2] = None
                pointer.type = 3
                pointer.children_count = 3
                pointer.children[0].type = 4
                pointer.children[0].children_count = 4
            elif pointer.parent.children[1].type == 2 and pointer.parent.children[2].type == 2:
                pointer = pointer.parent
                pointer.children[1].keys[1] = pointer.keys[1]
                pointer.children[1].items[1] = pointer.items[1]
                pointer.children[1].keys[2] = pointer.children[2].keys[0]
                pointer.children[1].items[2] = pointer.children[2].items[0]
                pointer.children[1].children[2] = pointer.children[2].children[0]
                pointer.children[1].children[3] = pointer.children[2].children[1]
                pointer.children[2] = pointer.children[3]
                pointer.children[3] = None
                pointer.children[1].children[2].parent = pointer.children[1]
                pointer.children[1].children[3].parent = pointer.children[1]
                pointer.keys[1] = pointer.keys[2]
                pointer.items[1] = pointer.items[2]
                pointer.keys[2] = None
                pointer.items[2] = None
                pointer.type = 3
                pointer.children_count = 3
                pointer.children[1].type = 4
                pointer.children[1].children_count = 4
            elif pointer.parent.children[2].type == 2 and pointer.parent.children[3].type == 2:
                pointer = pointer.parent
                pointer.children[2].keys[2] = pointer.children[3].keys[0]
                pointer.children[2].items[2] = pointer.children[3].items[0]
                pointer.children[2].keys[1] = pointer.keys[2]
                pointer.children[2].items[1] = pointer.items[2]
                pointer.children[2].children[2] = pointer.children[3].children[0]
                pointer.children[2].children[3] = pointer.children[3].children[1]
                pointer.children[2].children[2].parent = pointer.children[2]
                pointer.children[2].children[3].parent = pointer.children[2]
                pointer.children[3] = None
                pointer.keys[2] = None
                pointer.items[2] = None
                pointer.type = 3
                pointer.children_count = 3
                pointer.children[2].type = 4
                pointer.children[2].children_count = 4
            else:
                return False
        # Geen van allen werken
        else:
            return False
        return True

    def retrieveItem(self, key):
        self.pointer = self.root
        while(self.pointer.keys.count(key) == 0):
            if key < self.pointer.keys[0]:              # if smaller than first key
                self.pointer = self.pointer.children[0]
            elif key > self.pointer.keys[1]:            # if bigger than second key
                if self.pointer.children[3] != None:
                    if key > self.pointer.keys[3]:
                        self.pointer = self.pointer.children[3]
                    else:
                        self.pointer = self.pointer.children[2]
                else:
                    self.pointer = self.pointer.children[2]
            elif key < self.pointer.keys[1]:            # if smaller than second key
                self.pointer = self.pointer.children[1]
            else:
                return [None, False]
        i = 0
        while i < 4:
            if self.pointer.keys[i] == key:
                return [self.pointer.items[i], True]
            i += 1

    def inorderTraverse(self, functioncall = None):
        self.pointer = self.root
        output = []
        if self.pointer.children[0] != None:
            self.pointer = self.pointer.children[0]
            output += (inorderTraverse(self.pointer))
            self.pointer = self.pointer.parent
        output.append(self.pointer.keys[0])
        if self.pointer.children[1] != None:
            self.pointer = self.pointer.children[1]
            output += (inorderTraverse(self.pointer))
            self.pointer = self.pointer.parent
        if self.pointer.keys[1] != None:
            output.append(self.pointer.keys[1])
        if self.pointer.children[2] != None:
            self.pointer = self.pointer.children[2]
            output += (inorderTraverse(self.pointer))
            self.pointer = self.pointer.parent
        if self.pointer.keys[2] != None:
            output.append(self.pointer.keys[2])
        if self.pointer.children[3] != None:
            self.pointer = self.pointer.children[3]
            output += (inorderTraverse(self.pointer))
            self.pointer = self.pointer.parent
        output = list(dict.fromkeys(output))
        if functioncall == print:
            for i in output:
                print(i)
        return(output)

    def save(self):
        self.pointer = self.root
        output = {'root':[]}
        for i in self.pointer.keys:
            if i is not None:
                output['root'].append(i)
        if self.pointer.children[0] != None:
            output['children'] = []
        for i in self.pointer.children:
            if i is not None:
                output['children'].append(save(i))
        return output

    def load(self, dict):
        self.root = None
        self.pointer = None
        self.size = 0


    def split(self, pointer):
        if pointer == self.root:                                    # if root
            pointer.parent = Node(pointer.keys[1], pointer.items[1])
            pointer.parent.children[0] = Node(pointer.keys[0], pointer.items[0], pointer.parent)
            pointer.parent.children[1] = Node(pointer.keys[2], pointer.items[2], pointer.parent)
            pointer.parent.children[0].children[0] = pointer.children[0]
            pointer.parent.children[0].children[1] = pointer.children[1]
            pointer.parent.children[1].children[0] = pointer.children[2]
            pointer.parent.children[1].children[1] = pointer.children[3]
            if pointer.children[0] != None:
                pointer.children[0].parent = pointer.parent.children[0]
                pointer.children[0].parent.children_count = 1
            if pointer.children[1] != None:
                pointer.children[1].parent = pointer.parent.children[0]
                pointer.children[1].parent.children_count = 2
            if pointer.children[2] != None:
                pointer.children[2].parent = pointer.parent.children[1]
                pointer.children[2].parent.children_count = 1
            if pointer.children[3] != None:
                pointer.children[3].parent = pointer.parent.children[1]
                pointer.children[3].parent.children_count = 1
            self.root=pointer.parent
            pointer.parent.type = 2
            pointer.parent.children_count = 2
            return True
        if pointer.parent.type == 2:                                # if parent is 2-node
            if pointer.parent.children[0] == pointer:               # if left child
                pointer.parent.keys[1] = pointer.parent.keys[0]
                pointer.parent.items[1] = pointer.parent.items[0]
                pointer.parent.children[2] = pointer.parent.children[1]
                pointer.parent.keys[0] = pointer.keys[1]
                pointer.parent.items[0] = pointer.items[1]
                pointer.parent.children[0] = Node(pointer.keys[0], pointer.items[0], pointer.parent)
                pointer.parent.children[1] = Node(pointer.keys[2], pointer.items[2], pointer.parent)
                pointer.parent.children[0].children[0] = pointer.children[0]
                pointer.parent.children[0].children[1] = pointer.children[1]
                pointer.parent.children[1].children[0] = pointer.children[2]
                pointer.parent.children[1].children[1] = pointer.children[3]
                if pointer.children[0] != None:
                    pointer.children[0].parent = pointer.parent.children[0]
                if pointer.children[1] != None:
                    pointer.children[1].parent = pointer.parent.children[0]
                if pointer.children[2] != None:
                    pointer.children[2].parent = pointer.parent.children[1]
                if pointer.children[3] != None:
                    pointer.children[3].parent = pointer.parent.children[1]
                pointer.parent.type = 3
                pointer.parent.children_count = 3
                return True
            elif pointer.parent.children[1] == pointer:               # if right child
                pointer.parent.keys[1] = pointer.keys[1]
                pointer.parent.items[1] = pointer.items[1]
                pointer.parent.children[1] = Node(pointer.keys[0], pointer.items[0], pointer.parent)
                pointer.parent.children[2] = Node(pointer.keys[2], pointer.items[2], pointer.parent)
                pointer.parent.children[1].children[0] = pointer.children[0]
                pointer.parent.children[1].children[1] = pointer.children[1]
                pointer.parent.children[2].children[0] = pointer.children[2]
                pointer.parent.children[2].children[1] = pointer.children[3]
                if pointer.children[0] != None:
                    pointer.children[0].parent = pointer.parent.children[1]
                if pointer.children[1] != None:
                    pointer.children[1].parent = pointer.parent.children[1]
                if pointer.children[2] != None:
                    pointer.children[2].parent = pointer.parent.children[2]
                if pointer.children[3] != None:
                    pointer.children[3].parent = pointer.parent.children[2]
                pointer.parent.type = 3
                pointer.parent.children_count = 3
                return True
        elif pointer.parent.type == 3:                              # if parent is 3-node
            if pointer.parent.children[0] == pointer:               # if left child
                pointer.parent.keys[2] = pointer.parent.keys[1]
                pointer.parent.items[2] = pointer.parent.items[1]
                pointer.parent.keys[1] = pointer.parent.keys[0]
                pointer.parent.items[1] = pointer.parent.items[0]
                pointer.parent.children[3] = pointer.parent.children[2]
                pointer.parent.children[2] = pointer.parent.children[1]
                pointer.parent.keys[0] = pointer.keys[1]
                pointer.parent.items[0] = pointer.items[1]
                pointer.parent.children[0] = Node(pointer.keys[0], pointer.items[0], pointer.parent)
                pointer.parent.children[1] = Node(pointer.keys[2], pointer.items[2], pointer.parent)
                pointer.parent.children[0].children[0] = pointer.children[0]
                pointer.parent.children[0].children[1] = pointer.children[1]
                pointer.parent.children[1].children[0] = pointer.children[2]
                pointer.parent.children[1].children[1] = pointer.children[3]
                if pointer.children[0] != None:
                    pointer.children[0].parent = pointer.parent.children[0]
                if pointer.children[1] != None:
                    pointer.children[1].parent = pointer.parent.children[0]
                if pointer.children[2] != None:
                    pointer.children[2].parent = pointer.parent.children[1]
                if pointer.children[3] != None:
                    pointer.children[3].parent = pointer.parent.children[1]
                pointer.parent.type = 4
                pointer.parent.children_count = 4
                return True
            if pointer.parent.children[1] == pointer:               # if middle child
                pointer.parent.keys[2] = pointer.parent.keys[1]
                pointer.parent.keys[2] = pointer.parent.keys[1]
                pointer.parent.children[3] = pointer.parent.children[2]
                pointer.parent.children[1] = Node(pointer.keys[0], pointer.items[0], pointer.parent)
                pointer.parent.children[2] = Node(pointer.keys[2], pointer.items[2], pointer.parent)
                pointer.parent.children[1].children[0] = pointer.children[0]
                pointer.parent.children[1].children[1] = pointer.children[1]
                pointer.parent.children[2].children[0] = pointer.children[2]
                pointer.parent.children[2].children[1] = pointer.children[3]
                if pointer.children[0] != None:
                    pointer.children[0].parent = pointer.parent.children[1]
                if pointer.children[1] != None:
                    pointer.children[1].parent = pointer.parent.children[1]
                if pointer.children[2] != None:
                    pointer.children[2].parent = pointer.parent.children[2]
                if pointer.children[3] != None:
                    pointer.children[3].parent = pointer.parent.children[2]
                pointer.parent.type = 4
                pointer.parent.children_count = 4
                return True
            if pointer.parent.children[2] == pointer:               # if right child
                pointer.parent.keys[2] = pointer.keys[1]
                pointer.parent.items[2] = pointer.items[1]
                pointer.parent.children[2] = Node(pointer.keys[0], pointer.items[0], pointer.parent)
                pointer.parent.children[3] = Node(pointer.keys[2], pointer.items[2], pointer.parent)
                pointer.parent.children[2].children[0] = pointer.children[0]
                pointer.parent.children[2].children[1] = pointer.children[1]
                pointer.parent.children[3].children[0] = pointer.children[2]
                pointer.parent.children[3].children[1] = pointer.children[3]
                if pointer.children[0] != None:
                    pointer.children[0].parent = pointer.parent.children[2]
                if pointer.children[1] != None:
                    pointer.children[1].parent = pointer.parent.children[2]
                if pointer.children[2] != None:
                    pointer.children[2].parent = pointer.parent.children[3]
                if pointer.children[3] != None:
                    pointer.children[3].parent = pointer.parent.children[3]
                pointer.parent.type = 4
                pointer.parent.children_count = 4
                return True
        return False

def inorderTraverse(pointer):
    output = []
    if pointer.children[0] != None:
        pointer = pointer.children[0]
        output += (inorderTraverse(pointer))
        pointer = pointer.parent
    output.append(pointer.keys[0])
    if pointer.children[1] != None:
        pointer = pointer.children[1]
        output += (inorderTraverse(pointer))
        spointer = pointer.parent
    if pointer.keys[1] != None:
        output.append(pointer.keys[1])
    if pointer.children[2] != None:
        pointer = pointer.children[2]
        output += (inorderTraverse(pointer))
        pointer = pointer.parent
    if pointer.keys[2] != None:
        output.append(pointer.keys[2])
    if pointer.children[3] != None:
        pointer = pointer.children[3]
        output += (inorderTraverse(pointer))
        pointer = pointer.parent
    return (output)

def save(pointer):
    output = {'root': []}
    for i in pointer.keys:
        if i is not None:
            output['root'].append(i)
    if pointer.children[0] != None:
        output['children'] = []
    for i in pointer.children:
        if i is not None:
            output['children'].append(save(i))
    return output

class Node:
    def __init__(self, key, item, parent=None):
        self.keys = [key, None, None]
        self.items = [item, None, None]
        self.parent = parent
        self.children = [None, None, None, None]
        self.type = 2
        self.children_count = 0

#TESTCODE
"""
t = TwoThreeFourTree()
t.load({'root': [2, 5], 'children': [{'root': [1]}, {'root': [3, 4]}, {'root': [12, 15]}]})
t.insertItem(createTreeItem(3,"david"))
t.insertItem(createTreeItem(32,"mel"))
t.insertItem(createTreeItem(4,"sophie"))
t.insertItem(createTreeItem(15,"thomas"))
t.insertItem(createTreeItem(9,"martijn"))
t.insertItem(createTreeItem(0,"jer"))
t.save()
"""

