/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
    /**
     * @param {ListNode} head
     * @return {ListNode}
     */
    reverseList(head) {
        // if (head === null || (head?.next === null)) return head

        // let current = head.next
        // let prevCurrent = null
        // head.next = null

        // while (current !== null) {
        //     const currentNext = current.next
        //     current.next = prevCurrent || head
        //     prevCurrent = current
        //     current = currentNext
        // }

        // return prevCurrent

        if (head === null || (head?.next === null)) return head

        const newHead = this.reverseList(head.next)
        head.next.next = head
        head.next = null

        return newHead
    }
}
