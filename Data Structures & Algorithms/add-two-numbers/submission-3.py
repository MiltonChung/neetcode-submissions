# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carryOne = False
        curr1, curr2 = l1, l2
        head, resCurr = ListNode(), None

        while curr1 and curr2:
            nextNum, carryOne = self.carryFn(curr1.val + curr2.val, carryOne)
            
            if head.next is None:
                resCurr = ListNode(nextNum)
                head.next = resCurr
            else:
                newNode = ListNode(nextNum)
                resCurr.next = newNode
                resCurr = resCurr.next            

            curr1 = curr1.next
            curr2 = curr2.next

        while curr1:
            nextNum, carryOne = self.carryFn(curr1.val, carryOne)
            resCurr.next = ListNode(nextNum)
            resCurr = resCurr.next
            curr1 = curr1.next

        while curr2:
            nextNum, carryOne = self.carryFn(curr2.val, carryOne)
            resCurr.next = ListNode(nextNum)
            resCurr = resCurr.next
            curr2 = curr2.next
        
        if carryOne:
            resCurr.next = ListNode(1)
        
        return head.next

    def carryFn(self, nextNum, carryOne):
        if carryOne:
            nextNum += 1
            carryOne = False

        if nextNum >= 10:
            nextNum -= 10
            carryOne = True
        return [nextNum, carryOne]
