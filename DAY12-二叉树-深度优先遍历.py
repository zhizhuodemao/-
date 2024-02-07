# 前序遍历-递归-LC144_二叉树的前序遍历
# Definition for a binary tree node.
"""
1.确定递归函数的参数和返回值： 确定哪些参数是递归的过程中需要处理的，
那么就在递归函数里加上这个参数，
并且还要明确每次递归的返回值是什么进而确定递归函数的返回类型。
2.确定终止条件： 写完了递归算法, 运行的时候，经常会遇到栈溢出的错误，
就是没写终止条件或者终止条件写的不对，
操作系统也是用一个栈的结构来保存每一层递归的信息，如果递归没有终止，
操作系统的内存栈必然就会溢出。
3.确定单层递归的逻辑： 确定每一层递归需要处理的信息。在这里也就会重复调用自己来实现递归的过程。
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root):
        if not root:
            return []

        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)

        return [root.val] + left + right
    def inorderTraversal(self, root: TreeNode):
        if root is None:
            return []

        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)

        return left + [root.val] + right

    def postorderTraversal(self, root: TreeNode):
        if not root:
            return []

        left = self.postorderTraversal(root.left)
        right = self.postorderTraversal(root.right)

        return left + right + [root.val]

