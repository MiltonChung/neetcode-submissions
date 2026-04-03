# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carryOne = False
        curr1 = l1
        curr2 = l2
        head = ListNode()
        resCurr = None

        while curr1 and curr2:
            nextNum = curr1.val + curr2.val
            if carryOne:
                nextNum += 1
                carryOne = False

            if nextNum >= 10:
                nextNum -= 10
                carryOne = True

            if head.next is None:
                resCurr = ListNode(nextNum)
                head.next = resCurr
            else:
                newNode = ListNode(nextNum)
                resCurr.next = newNode
                resCurr = resCurr.next            

            if carryOne and curr1.next is None and curr2.next is None:
                resCurr.next = ListNode(1)
            
            curr1 = curr1.next
            curr2 = curr2.next

        while curr1:
            nextNum = curr1.val
            if carryOne:
                nextNum += 1
                carryOne = False

            if nextNum >= 10:
                nextNum -= 10
                carryOne = True

            newNode = ListNode(nextNum)
            resCurr.next = newNode
            resCurr = resCurr.next
            curr1 = curr1.next

        while curr2:
            nextNum = curr2.val
            if carryOne:
                nextNum += 1
                carryOne = False

            if nextNum >= 10:
                nextNum -= 10
                carryOne = True

            newNode = ListNode(nextNum)
            resCurr.next = newNode
            resCurr = resCurr.next
            curr2 = curr2.next
        
        if carryOne:
            resCurr.next = ListNode(1)
        
        return head.next
