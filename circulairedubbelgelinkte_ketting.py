#============================================================================
# Name        : circulairedubbelgelinkte_ketting.py
# Author      : Daan Thielemans
# Version     : 1.0
# Copyright   : GAS - BA1 Informatica - Daan Thielemans - University of Antwerp
# Description : Doubly circular linked list implementation in python
#============================================================================

class LinkedChain:
    def __init__(self):                             #create
        self.head = None
        self.pointer = None
        self.size = 0

    def isEmpty(self):                              #isEmpty
        if self.size==0:
            return True
        return False

    def getLength(self):                            #getLength
        return self.size

    def insert(self, positie, newItem=None):        #insert
        self.pointer=self.head
        #kijk of index klopt
        if self.size+1 < positie or positie < 1 :
            return False
        #als er nog niks in de ketting zit
        if self.head == None:
            self.head = Node(1,None,None,newItem)
            self.head.vorige_node=self.head
            self.head.volgende_node=self.head
            self.pointer = self.head
            self.size += 1
            return True
        #insert code
        else:
            #zet alle indexen van nodes na nieuwe node op +1
            if positie != self.size+1:
                while (self.pointer.positie != positie+1):
                    self.pointer=self.pointer.vorige_node
                    self.pointer.positie += 1
            #maak nieuwe node aan
            nieuwe_positie=self.pointer.positie-1
            if positie == self.size+1:
                nieuwe_positie=self.size+1
            self.pointer.vorige_node=Node(nieuwe_positie, self.pointer, self.pointer.vorige_node, newItem)
            #zet pointer op nieuwe node
            self.pointer = self.pointer.vorige_node
            if positie == 1:
                self.head=self.pointer
            #zet volgende_pointer van node voor nieuwe node op nieuwe node
            self.pointer = self.pointer.vorige_node
            self.pointer.volgende_node=self.pointer.volgende_node.vorige_node
            #zet pointer op head
            self.pointer=self.head
        #size + 1
        self.size += 1
        return True

    def delete(self, positie):                      #delete
        self.pointer=self.head
        #kijk of index klopt
        if self.size < positie or positie < 1:
            return False
        #zet alle indexen van nodes na nieuwe node op -1
        if positie != self.size-1 and positie != 1:
            while (self.pointer.positie != positie):
                self.pointer = self.pointer.vorige_node
                self.pointer.positie -= 1
        if positie != self.size-1 and positie == 1:
            self.pointer = self.pointer.vorige_node
            self.pointer.positie -= 1
            while (self.pointer.positie != positie):
                self.pointer = self.pointer.vorige_node
                self.pointer.positie -= 1
        #zet pointers van node voor en na verwijderde node op elkaar
        self.pointer.vorige_node=self.pointer.vorige_node.vorige_node
        self.pointer.vorige_node.volgende_node=self.pointer
        if positie == 1:
            self.head=self.pointer
        # zet pointer op head
        self.pointer=self.head
        # size - 1
        self.size -= 1
        return True

    def retrieve(self, positie):                    #retrieve
        self.pointer=self.head
        #kijk of index klopt
        if self.size < positie or positie < 0:
            return [None, False]
        #retrieve
        while (self.pointer.positie != positie):
            self.pointer = self.pointer.volgende_node
        output=self.pointer.inhoud
        # zet pointer op head
        self.pointer = self.head
        return [output, True]

    def save(self):
        out = []
        self.pointer = self.head
        while(True):
            out.append(self.pointer.inhoud)
            self.pointer = self.pointer.volgende_node
            if self.pointer == self.head:
                return out

    def load(self, list):
        self.head = None
        self.pointer = None
        self.size = 0
        for i in list:
            self.insert(self.size+1,i)
        return True

class Node:
    def __init__(self, positie, volgende_node, vorige_node, inhoud = None):
        self.positie = positie
        self.inhoud = inhoud
        self.volgende_node = volgende_node
        self.vorige_node = vorige_node

l = LinkedChain()
print(l.isEmpty())
print(l.getLength())
print(l.retrieve(4)[1])
print(l.insert(4,500))
print(l.isEmpty())
print(l.insert(1,500))
print(l.retrieve(1)[0])
print(l.retrieve(1)[1])
print(l.save())
print(l.insert(1,600))
print(l.save())
l.load([10,-9,15])
l.insert(3,20)
print(l.delete(0))
print(l.save())
print(l.delete(1))
print(l.save())