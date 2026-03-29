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
     * @param {ListNode} list1
     * @param {ListNode} list2
     * @return {ListNode}
     */
    mergeTwoLists(list1, list2) {
        const dummy = new ListNode()
        let result = dummy

        while (list1 && list2) {
            if (list1.val <= list2.val) {
                result.next = list1
                list1 = list1.next
            } else {
                result.next = list2
                list2 = list2.next
            }
            
            result = result.next
        }

        if (list1) result.next = list1
        else if (list2) result.next = list2

        return dummy.next
    }
}
