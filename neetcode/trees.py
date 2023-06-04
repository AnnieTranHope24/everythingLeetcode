# Given the root of a binary tree, return the length of the diameter of the tree.
#
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
# This path may or may not pass through the root.
#
# The length of a path between two nodes is represented by the number of edges between them.
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            nonlocal res
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            res = max(left + right, res)

            return 1 + max(left, right)

        dfs(root)
        return res

# Given a binary tree, determine if it is
# height-balanced

# A height-balanced binary tree is a binary tree in which
# the depth of the two subtrees of every node never differs by more than one.

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(self, root):
            if not root:
                return True, -1
            else:
                balancedL, hL = height(root.left)
                balancedR, hR = height(root.right)
                return (balancedL and balancedR and (abs(hL - hR) <= 1)), 1 + max(hL, hR)

        re, h = height(root)
        return re

# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
#
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
