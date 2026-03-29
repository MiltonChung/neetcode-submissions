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
        console.log(this.minValue, val)
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
            this.minValue = this.stack[this.stack.length - 1].minValue
            console.log('min ', this.minValue)
        } else {
            this.minValue = null
            console.log('min is null')
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
        console.log(this.stack[this.stack.length - 1])
        return this.stack[this.stack.length - 1].minValue
    }
}
