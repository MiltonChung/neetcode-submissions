"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None: return None
        
        copyList = {}
        curr = head

        while curr:
            newNode = Node(curr.val)
            copyList[curr] = newNode
            curr = curr.next

        curr = head
        while curr:
            copyNode = copyList[curr]
            copyNode.next = copyList[curr.next] if curr.next is not None else None
            copyNode.random = copyList[curr.random] if curr.random is not None else None
            curr = curr.next

        return copyList[head]
