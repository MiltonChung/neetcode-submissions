class Pair:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class HashTable:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.map = []
        for i in range(0, capacity):
            self.map.append(Pair(0, 0))

    def insert(self, key: int, value: int) -> None:
        index = self.hash(key)
        curr = self.map[index].next

        while curr is not None:
            if curr.key == key:
                curr.val = value
                return
            curr = curr.next

        newNode = Pair(key, value)
        newNode.next = self.map[index].next
        self.map[index].next = newNode
        self.size += 1

        # if curr == None:
        #     self.map[index].next = newNode
        #     self.size += 1
        # elif curr.key == key:
        #     curr.val = value
        # else:
        #     while curr.next != None:
        #         if curr.key == key:
        #             curr.val = value
        #         curr = self.map[index].next
        #     curr.next = newNode
        #     self.size += 1
        print(self.size)
        if self.size >= self.capacity // 2:
            self.resize()

    def get(self, key: int) -> int:
        index = self.hash(key)
        curr = self.map[index].next

        while curr is not None:
            if curr.key == key:
                return curr.val
            curr = curr.next
        return -1

        # if curr == None:
        #     return -1
        # elif curr.key == key:
        #     return curr.val
        # else:
        #     while curr.next != None:
        #         if curr.key == key:
        #             return curr.val
        #         curr = self.map[index].next
        #     return -1

    def remove(self, key: int) -> bool:
        index = self.hash(key)
        curr = self.map[index].next

        if curr == None:
            return False
        elif curr.key == key:
            if curr.next:
                self.map[index].next = curr.next
            else:
                self.map[index].next = None
            self.size -= 1
            return True
        else:
            prev = self.map[index]
            while curr.next != None:
                if curr.key == key:
                    if curr.next:
                        prev.next = curr.next
                    else:
                        curr.next = None
                    self.size -= 1
                    return True
                prev = curr
                curr = curr.next
            return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        print('resize')
        self.capacity = 2 * self.capacity
        self.size = 0
        newMap = []
        for i in range(self.capacity):
            newMap.append(Pair(0, 0))
        
        oldMap = self.map
        self.map = newMap
        for pair in oldMap:
            curr = pair.next
            while curr is not None:
                self.insert(curr.key, curr.val)
                curr = curr.next

    def hash(self, key) -> None:
        return key % self.capacity


