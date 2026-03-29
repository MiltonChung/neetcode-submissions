class Node {
    constructor(key, val) {
        this.key = key
        this.val = val
        this.left = null
        this.right = null
    }
}

class TreeMap {
    constructor() {
        this.root = null
    }

    /**
     * @param {number} key
     * @param {number} val
     * @returns {void}
     */
    insert(key, val) {
        const newNode = new Node(key, val)

        const insertHelper = (root, node) => {
            if (root === null) {
                return node
            }

            if (node.key > root.key) {
                root.right = insertHelper(root.right, node)
            } else if (node.key < root.key) {
                root.left = insertHelper(root.left, node)
            } else if (node.key === root.key) {
                root.val = node.val
            }

            return root
        }

        if (this.root === null) {
            this.root = newNode
            return
        }

        insertHelper(this.root, newNode)
    }

    /**
     * @param {number} key
     * @returns {number}
     */
    get(key) {
        const getHelper = (root, key) => {
            if (root === null) return root

            if (key > root.key) {
                return getHelper(root.right, key)
            } else if (key < root.key) {
                return getHelper(root.left, key)
            }
            
            return root.val
        }

        const res = getHelper(this.root, key)
        
        if (res) return res
        else return -1
    }

    /**
     * @returns {number}
     */
    getMin() {
        if (this.root === null) return -1

        let curr = this.root
        while (curr !== null && curr.left !== null) {
            curr = curr.left
        }
        return curr.val
    }

    /**
     * @returns {number}
     */
    getMax() {
        if (this.root === null) return -1

        let curr = this.root
        while (curr !== null && curr.right !== null) {
            curr = curr.right
        }
        return curr.val
    }

    /**
     * @param {number} key
     * @returns {void}
     */
    remove(key) {
        const getMinValueGivenNode = (root) => {
            let curr = root
            while (curr !== null && curr.left !== null) {
                curr = curr.left
            }
            return curr
        }

        const removeHelper = (root, key) => {
            if (root === null) return root

            if (key > root.key) {
                root.right = removeHelper(root.right, key)
            } else if (key < root.key) {
                root.left = removeHelper(root.left, key)
            } else {
                // node has 0 or 1 child
                // node has 2 children
                if (root.left === null) {
                    return root.right
                } else if (root.right === null) {
                    return root.left
                } else {
                    const minNode = getMinValueGivenNode(root.right)
                    root.key = minNode.key
                    root.val = minNode.val
                    root.right = removeHelper(root.right, minNode.key)
                }
            }
            return root
        }
        // console.log(this.root)
        this.root = removeHelper(this.root, key)
    }

    /**
     * @returns {number[]}
     */
    getInorderKeys() {
        // DFS inorder traversal
        let res = []

        const inorder = (root) => {
            if (root === null) return 

            inorder(root.left)
            res.push(root.key)
            inorder(root.right)
        }

        inorder(this.root)
        return res
    }
}
