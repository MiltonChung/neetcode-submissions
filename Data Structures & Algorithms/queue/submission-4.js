class ListNode {
    constructor(value) {
        this.value = value
        this.next = null
        this.prev = null
    }
}

class MyDeque {
    constructor() {
        this.head = new ListNode(-1)
        this.tail = this.head
    }

    /**
     * @return {boolean}
     */
    isEmpty() {
        return !Boolean(this.head.next)
    }

    /**
     * @param {number} value
     */
    append(value) {
        const newNode = new ListNode(value)

        this.tail.next = newNode
        newNode.prev = this.tail
        this.tail = newNode
    }

    /**
     * @param {number} value
     * @return {void}
     */
    appendleft(value) {
        const newNode = new ListNode(value)

        if (this.head.next) {
            this.head.next.prev = newNode
        } else {
            this.tail = newNode
        }

        newNode.next = this.head.next
        newNode.prev = this.head
        this.head.next = newNode

    }

    /**
     * @return {number}
     */
    pop() {
        if (this.tail === this.head) {
            return -1
        }

        const toBePopped = this.tail
        const prev = this.tail.prev
        prev.next = null
        this.tail = prev

        return toBePopped.value
    }

    /**
     * @return {number}
     */
    popleft() {
        if (this.tail === this.head) {
            return -1
        }

        const toBePopped = this.head.next
        const next = this.head.next.next
        if (next) {
            this.head.next = next
            next.prev = this.head
        } else {
            this.head.next = null
            this.tail = this.head
        }

        return toBePopped.value
    }
}
