#============================================================================
# Name        : MyStack.py
# Author      : David Scalais
# Copyright   : GAS - BA1 Informatica - David Scalais - University of Antwerp
# Description : link-based Stack implementation in python
#============================================================================

class StackItemType:

    def __init__(self, value, next=None):
        """
        creëert een item met als attribute een value en een next
        preconditie:
        postconditie: een item met een value en een next (=None) wordt aangemaakt
        """
        self.value = value
        self.next = next


class MyStack:
    def __init__(self):
        """
        Creëert een lege stack

        preconditie:
        postconditie: er is een stack aangemaakt en die is leeg (size == 0)


        """
        self.top = None

    def isEmpty(self):
        """
        Bepaalt of een stack leeg is.
        preconditie:
        postconditie:
        :return: True als de stack leeg is
        """
        succes = [True]
        if self.top == None:
            return succes[0]
        else:
            succes.append(False)
            return succes[1]

    def push(self, newItem):
        """
        Voegt het element ‘newItem’ toe op de top van een stack.

        preconditie: stack moet worden aangemaakt
        postconditie: nieuw item wordt toegevoegd
        :param newItem:
        :return: True
        """

        test = StackItemType(newItem)

        if(self.top == None):
            self.top = test

        else:
            test.next = self.top
            self.top = test

        return True

    def pop(self):
        """
        Verwijdert de top van een stack, d.i. het laatst toegevoegde element.
        preconditie: een item moet in de stack zijn.
        postconditie: laatst toegevoegde element wordt verwijdert.
        :return: False als stack leeg is
        Geeft de laatst toegevoegde element weer
        """
        if(self.isEmpty()):
            return (None, False)
        else:
            StackTop = self.top.value
            self.top = self.top.next
            return (StackTop, False)

    def getTop(self):
        """
        Plaatst de top van een stack (d.i. het laatst toegevoegde element) in
        ‘stackTop’ en laat de stack ongewijzigd
        preconditie: stack mag niet leeg zijn
        postconditie:
        :return: False als stack leeg is
        True
        """

        if self.top == None:

            return (None, False)
        else:
            StackTop = self.top.value
            return (StackTop, False)

    def save(self):
        omgekeerd = []
        current = self.top
        while(current != None):
            omgekeerd.append(current.value)
            current = current.next
        return omgekeerd[::-1]

    def load(self, stack):
        while(self.isEmpty() != True):
            self.pop()
        else:
            for item in stack:
                self.push(item)