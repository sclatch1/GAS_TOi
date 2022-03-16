# linkbased
class QueueItemType:
    def __init__(self, value, next=None, previous=None):

        self.value = value
        self.next = next

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
        if self.front == None:
            newItem.next = self.front
            self.front = newItem
        else:
            newItem.next = self.back
            self.back = newItem

        return True
    def dequeue(self):
        """
        Verwijdert de kop van de queue, d.i. het eerst toegevoegde element
        preconditie: queue mag niet leeg zijn
        postcondtie: eerst toegevoegde element wordt verwijdert
        :return: eerst toegevoegde element
        """
        if self.front == None:
            return False
        else:
            self.front = self.front.next
            return self.front
    def getFront(self):
        """
        Plaatst de kop van een queue (d.i. het eerst toegevoegde element) in
        ‘queueFront’ en laat de queue ongewijzigd.
        preconditie: moet een kop hebben
        postconditie:
        :return: True
        """



