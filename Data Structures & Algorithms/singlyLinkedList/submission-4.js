class ListNode {
    constructor(value, next = null) {
        this.value = value
        this.next = next
    }
}

class LinkedList {
    constructor() {
        this.head = new ListNode(-1)
        this.tail = this.head
    }

    /**
     * @param {number} index
     * @return {number}
     */
    get(index) {
        let i = 0;
        let cur = this.head.next

        while (cur) {
            if (i === index) {
                return cur.value
            }

            i++
            cur = cur.next
        }

        return -1
    }

    /**
     * @param {number} val
     * @return {void}
     */
    insertHead(val) {
        const listNode = new ListNode(val)

        listNode.next = this.head.next
        this.head.next = listNode

        if (!listNode.next) {
            this.tail = listNode
        }
    }

    /**
     * @param {number} val
     * @return {void}
     */
    insertTail(val) {
        const listNode = new ListNode(val)
        this.tail.next = listNode
        this.tail = listNode
    }

    /**
     * @param {number} index
     * @return {boolean}
     */
    remove(index) {
        let i = 0;
        let cur = this.head
        let result = false

        while ((i < index) && cur) {
            i++
            cur = cur.next
        }

        if (cur && cur.next) {
            if (cur.next === this.tail) {
                this.tail = cur;
            }
            cur.next = cur.next.next;
            result = true;
        }

        return result
    }

    /**
     * @return {number[]}
     */
    getValues() {
        let cur = this.head.next
        let values = []

        while (cur) {
            values.push(cur.value)
            cur = cur.next
        }

        return values
    }
}
