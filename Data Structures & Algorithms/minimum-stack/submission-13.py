class Node:
    def __init__(self, value=None):
        self.value = value
        self.currMin = float('inf')
        self.prev = None
        self.next = None

class MinStack:

    def __init__(self):
        self.startDummy = Node()
        self.endDummy = Node()
        self.startDummy.next = self.endDummy
        self.endDummy.prev = self.startDummy

    def push(self, val: int) -> None:
        newNode = Node(val)
        lastNode = self.endDummy.prev
        newNode.currMin = min(lastNode.currMin, val)
        if self.endDummy.prev == self.startDummy:
            self.startDummy.next = newNode
            newNode.prev = self.startDummy
        else:
            lastNode.next = newNode
            newNode.prev = lastNode
        newNode.next = self.endDummy
        self.endDummy.prev = newNode

    def pop(self) -> None:
        lastNode = self.endDummy.prev
        newLastNode = lastNode.prev
        newLastNode.next = self.endDummy
        self.endDummy.prev = newLastNode

    def top(self) -> int:
        return self.endDummy.prev.value

    def getMin(self) -> int:
        return self.endDummy.prev.currMin