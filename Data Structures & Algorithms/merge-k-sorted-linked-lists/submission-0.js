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
     * @param {ListNode[]} lists
     * @return {ListNode}
     */
    mergeKLists(lists) {
        if (lists.length < 1) return null

        for (let i = 1; i < lists.length; i++) {
            lists[i] = this.merge(lists[i], lists[i - 1])
        }

        return lists[lists.length - 1]
    }

    merge(list1, list2) {
        const dummy = new ListNode(0)
        let tail = dummy

        while (list1 && list2) {
            if (list1.val <= list2.val) {
                tail.next = list1
                list1 = list1.next
            } else {
                tail.next = list2
                list2 = list2.next
            }
            tail = tail.next
        }

        while (list1) {
            tail.next = list1
            list1 = list1.next
            tail = tail.next
        }

        while (list2) {
            tail.next = list2
            list2 = list2.next
            tail = tail.next
        }

        return dummy.next
    }
}
