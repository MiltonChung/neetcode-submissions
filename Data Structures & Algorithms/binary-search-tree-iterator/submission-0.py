# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        stack = []
        curr = root
        self.inorder = []
        self.pointer = -1

        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                self.inorder.append(curr)
                curr = curr.right

    def next(self) -> int:
        self.pointer += 1
        return self.inorder[self.pointer].val

    def hasNext(self) -> bool:
        if self.pointer + 1 >= len(self.inorder):
            return False
        return True

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()