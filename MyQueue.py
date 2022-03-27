#============================================================================
# Name        : MyQueue.py
# Author      : David Scalais
# Copyright   : GAS - BA1 Informatica - David Scalais - University of Antwerp
# Description : link-based Queue implementation in python
#============================================================================

class QueueItemType:
    def __init__(self, value):

        self.value = value
        self.next = None

class Pointer:
    def __init__(self):

        self.next = None

class MyQueue:
    def __init__(self):
        """
        Creëert een lege queue

        preconditie:
        postconditie: er is een stack aangemaakt en die is leeg (size == 0)
        """
        self.front = None
        self.back = None


    def isEmpty(self):
        """
        Bepaalt of een queue leeg is
        preconditie:
        postconditie
        :return: True als leeg is
        False als het niet leeg is
        """
        if self.front == None:
            return True
        else:
            return False

    def enqueue(self, newItem):
        """
        Voegt het element ‘newItem’ toe aan het eind (de staart) van de queue
        preconditie: queue moet worden aangemaakt
        postconditie: item wordt aan de staat toegevoegd
        :param newItem:
        :return: True
        """
        temp = QueueItemType(newItem)


        if self.back == None:
            self.front = self.back = temp
            return True
        self.back.next = temp
        self.back = temp
        return True
    def dequeue(self):
        """
        Verwijdert de kop van de queue, d.i. het eerst toegevoegde element
        preconditie: queue mag niet leeg zijn
        postcondtie: eerst toegevoegde element wordt verwijdert
        :return: eerst toegevoegde element
        """
        if self.isEmpty():
            return (None, False)

        else:
            temp = self.front
            self.front = temp.next
            return (temp.value, True)
    def getFront(self):
        """
        Plaatst de kop van een queue (d.i. het eerst toegevoegde element) in
        ‘queueFront’ en laat de queue ongewijzigd.
        preconditie: moet een kop hebben
        postconditie:
        :return: True
        """
        if self.isEmpty():
            return (None, False)
        else:
            queueFront = self.front.value
            return (queueFront, True)

    def save(self):
        omgekeerd = []

        current = self.front
        while (current != self.back):
            omgekeerd.append(current.value)
            current = current.next
        omgekeerd.append(self.back.value)
        return omgekeerd[::-1]

    def load(self, list):
        while (self.isEmpty() == False):
            self.dequeue()
        self.back = None

        test = list[::-1]
        for item in test:
                self.enqueue(item)


