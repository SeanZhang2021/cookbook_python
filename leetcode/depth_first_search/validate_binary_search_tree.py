# Given a binary tree, determine if it is a valid binary search tree (BST).
#
# Assume a BST is defined as follows:
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
# Example 1:

# 2
# /\
# 1 3

# Input: [2,1,3]
# Output: true
# Example 2:

# 5
# /\
# 1 4
#   /\ 36
# Input: [5,1,4,null,null,3,6] [5,3,6,1,4,None,7]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
# 题目大意
# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。假设一个二叉搜索树具有如下特征:
#   节点的左子树只包含小于当前节点的数。
#   节点的右子树只包含大于当前节点的数。
#   所有左子树和右子树自身必须也是二叉搜索树。
# 解题思路
# 判断一个树是否是 BST，按照定义递归判断即可
import math

class BinaryTree:
    def __init__(self, value, right, left):
        self.value = value
        self.right = right
        self.left = left
    def getValue(self):
        return self.value
    def getLeftTree(self):
        return self.left

class Solution:
    def buildTree(self, nums: list) -> BinaryTree:
        # 树根，每创建一个节点，维护到树根中
        print("start build tree")
        currentRoot: BinaryTree = BinaryTree(None, None, None)
        self.fulfillTree(nums, currentRoot, 0)
        print("build tree finish!")
        return currentRoot

    def fulfillTree(self, nums: list, currentRoot: BinaryTree, currentIndex: int):
        # 计算左右节点在数组中的下标
        leftIndex = currentIndex * 2 + 1
        rightIndex = currentIndex * 2 + 2      
        # 赋值
        currentRoot.value = nums[currentIndex]
        print("fulfill:", currentRoot.value)
        # 递归初始化子树，递归出口：在数组范围内操作
        if leftIndex <= len(nums) - 1 and nums[leftIndex]!=None:
            leftTree = BinaryTree(None, None, None)
            currentRoot.left= leftTree
            self.fulfillTree(nums, leftTree, leftIndex)
        if rightIndex <= len(nums) - 1 and nums[rightIndex]!=None:
            rightTree = BinaryTree(None, None, None) 
            currentRoot.right  = rightTree 
            self.fulfillTree(nums, rightTree, rightIndex)
        return

    def depthSearchTree(self, root: BinaryTree, min, max) -> bool:
        if (root == None):
            return True
        val: int = root.value
        return val > min and val < max and self.depthSearchTree(root.left, min, val) and self.depthSearchTree(root.right, val, max)

    def isValid(self, nums: list) -> bool:
        # python的正负无穷
        return self.depthSearchTree(self.buildTree(nums), float('-inf'),
                                    float('inf'))

if __name__ == "__main__":
    ret = Solution().isValid([5,3,6,1,4,None,7])
    print(ret)
