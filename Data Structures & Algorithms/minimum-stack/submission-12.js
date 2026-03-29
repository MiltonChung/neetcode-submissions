class MinStack {
    constructor() {
        this.stack = []
        this.minValue = null
    }

    /**
     * @param {number} val
     * @return {void}
     */
    push(val) {
        if (this.minValue === null || this.minValue > val) {
            this.minValue = val
        }
        this.stack.push({
            value: val,
            minValue: this.minValue
        })
    }

    /**
     * @return {void}
     */
    pop() {
        this.stack.pop()
        if (this.stack.length > 0) {
            this.minValue = this.getMin()
        } else {
            this.minValue = null
        }
    }

    /**
     * @return {number}
     */
    top() {
        return this.stack[this.stack.length - 1].value
    }

    /**
     * @return {number}
     */
    getMin() {
        return this.stack[this.stack.length - 1].minValue
    }
}
