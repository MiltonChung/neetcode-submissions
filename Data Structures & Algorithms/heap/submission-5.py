class MinHeap:
    
    def __init__(self):
        self.heap = [0]

    def push(self, val: int) -> None:
        self.heap.append(val)
        self._bubble_up(len(self.heap) - 1)
        
    def pop(self) -> int:
        if len(self.heap) == 1:
            return -1
        if len(self.heap) == 2:
            return  self.heap.pop()

        res = self.heap[1]
        self.heap[1] = self.heap.pop()
        self._bubble_down(1)
        
        return res

    def top(self) -> int:
        if len(self.heap) == 1:
            return -1
        else:
            return self.heap[1]

    def heapify(self, nums: List[int]) -> None:
        self.heap = [0] + nums

        i = (len(self.heap) - 1 ) // 2
        while i > 0:
            self._bubble_down(i)
            i = i - 1

    def _bubble_down(self, i: int) -> None:
        while i * 2 < len(self.heap):
            if 2*i + 1 < len(self.heap) and self.heap[i * 2 + 1] < self.heap[i * 2] and self.heap[i] > self.heap[i * 2 + 1]:
                temp = self.heap[i]
                self.heap[i] = self.heap[i*2 + 1]
                self.heap[i*2 + 1] = temp
                i = i * 2 + 1
            elif self.heap[i] > self.heap[i * 2]:
                temp = self.heap[i]
                self.heap[i] = self.heap[i*2]
                self.heap[i*2] = temp
                i = i * 2
            else:
                break

    def _bubble_up(self, i: int) -> None:
        while i > 1 and self.heap[i] < self.heap[i // 2]:
            temp = self.heap[i]
            self.heap[i] = self.heap[i // 2]
            self.heap[i // 2] = temp
            i = i // 2


        