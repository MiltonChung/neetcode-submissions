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
        if (head === null || (head?.next === null)) return head

        let current = head.next
        let prevCurent = null
        head.next = null

        console.log(current, prevCurent, head)
        while (current !== null) {
            let tempCurrent = current.next
            current.next = prevCurent || head
            console.log(current, tempCurrent)
            prevCurent = current
            current = tempCurrent
            console.log(current, prevCurent)

            // if (tempCurrent === null) {
            //     head = current
            // }
            // break
            // if (prevCurent.next === head.next) head.next = null
        }
        console.log(prevCurent, current)

        return prevCurent
    }
}
