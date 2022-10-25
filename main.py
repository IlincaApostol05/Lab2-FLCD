class symbolTable:

    def __init__(self, size=10):
        self._items = [None] * size
        self._size = size

    def getSize(self):
        return self._size

    def getItems(self):
        return self._items

    def hashCode(self, key):
        return hash(key) % self._size

    def getValue(self, key):
        hashValue = self.hashCode(key)
        if self._items[hashValue] is None:
            return None
        else:
            for k in self._items[hashValue]:
                if k == key:
                    return hashValue
            return None

    def addValue(self, key):
        hashValue = self.hashCode(key)
        if self._items[hashValue] is None:  # if the position is empty
            self._items[hashValue] = []
            self._items[hashValue].append(key)
        else:
            for k in self._items[hashValue]:  # if the element already exists
                if k == key:
                    break
            else:
                self._items[hashValue].append(key)  # the position is not empty
        return hashValue

    def deleteValue(self, key):
        hashValue = self.hashCode(key)
        if self._items[hashValue] is None:       #if the position has no elements
            raise Exception('nothing to delete')
        else:
            for i, k in enumerate(self._items[hashValue]):   #else searching through the elements of that position
                if k == key:
                    del self._items[hashValue][i]
                    break
            else:
                raise Exception('nothing to delete')

    def __str__(self):
        return str(self._items)


def main():
    tableIdentifiers = symbolTable()
    print("The initial Identifiers table:")
    print(tableIdentifiers)
    print("-----------------------------------------------------------")
    tableIdentifiers.addValue("a")
    tableIdentifiers.addValue("b")
    tableIdentifiers.addValue("c")
    tableIdentifiers.addValue("d")
    print("The table Identifiers after adding values:")
    print(tableIdentifiers)
    print("-----------------------------------------------------------")
    print("The table Identifiers after deleting an element:")
    tableIdentifiers.deleteValue("b")
    print(tableIdentifiers)
    print("-----------------------------------------------------------")
    tableConstants = symbolTable()
    print("The initial Constants table:")
    print(tableConstants)
    print("-----------------------------------------------------------")
    tableConstants.addValue("a")
    tableConstants.addValue("b")
    print("The table Constants after adding values:")
    print(tableConstants)
    print("-----------------------------------------------------------")
    print("The table Constants after deleting an element:")
    tableConstants.deleteValue("a")
    print(tableConstants)


main()
