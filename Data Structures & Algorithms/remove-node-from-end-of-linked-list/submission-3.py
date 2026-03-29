# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        listLength = 0
        curr = head

        while curr:
            curr = curr.next
            listLength += 1

        indexToDelete = listLength - n

        # beginning
        if indexToDelete == 0:
            head = head.next
            return head

        curr = head
        currIndex = 0
        prev = None
        while curr:
            # end
            if indexToDelete == (listLength - 1) and currIndex == indexToDelete - 1:
                curr.next = None
                return head

            # middle
            if currIndex == indexToDelete - 1:
                prev = curr
            elif currIndex == indexToDelete + 1:
                prev.next = curr
                return head

            curr = curr.next
            currIndex += 1
        