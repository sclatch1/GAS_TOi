# linkbased
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
        if self.top == None:
            return True
        else:
            return False

    def push(self, newItem):
        """
        Voegt het element ‘newItem’ toe op de top van een stack.

        preconditie: stack moet worden aangemaakt
        postconditie: nieuw item wordt toegevoegd
        :param newItem:
        :return: True
        """
        newItem.next = self.top
        self.top = newItem
        return True
    def pop(self):
        """
        Verwijdert de top van een stack, d.i. het laatst toegevoegde element.
        preconditie: een item moet in de stack zijn.
        postconditie: laatst toegevoegde element wordt verwijdert.
        :return: False als stack leeg is
        Geeft de laatst toegevoegde element weer
        """
        if self.top == None:
            return False
        else:
            self.top = self.top.next
            return self.top
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
            return False
        else:
            self.stackTop = self.top
            return True


