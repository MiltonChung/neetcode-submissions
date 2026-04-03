# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carryOne = False
        dummy = ListNode()
        resCurr = dummy

        while l1 and l2:
            nextNum, carryOne = self.carryFn(l1.val + l2.val, carryOne)
            
            resCurr.next = ListNode(nextNum)
            resCurr = resCurr.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            nextNum, carryOne = self.carryFn(l1.val, carryOne)
            resCurr.next = ListNode(nextNum)
            resCurr = resCurr.next
            l1 = l1.next

        while l2:
            nextNum, carryOne = self.carryFn(l2.val, carryOne)
            resCurr.next = ListNode(nextNum)
            resCurr = resCurr.next
            l2 = l2.next
        
        if carryOne:
            resCurr.next = ListNode(1)
        
        return dummy.next

    def carryFn(self, nextNum, carryOne):
        if carryOne:
            nextNum += 1
            carryOne = False

        if nextNum >= 10:
            nextNum -= 10
            carryOne = True
        return [nextNum, carryOne]
