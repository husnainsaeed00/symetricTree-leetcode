class Solution(object):
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    def isMirror(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False
        if node1.val != node2.val:
            return False

        return self.isMirror(node1.left, node2.right) and self.isMirror(node1.right, node2.left)

    def isSymmetric(self, root):
        if root is None:
            return True

        return self.isMirror(root.left, root.right)


# Example usage:
# Creating a symmetric binary tree
root = Solution.TreeNode(1)
root.left = Solution.TreeNode(2)
root.right = Solution.TreeNode(2)
root.left.left = Solution.TreeNode(3)
root.left.right = Solution.TreeNode(4)
root.right.left = Solution.TreeNode(4)
root.right.right = Solution.TreeNode(3)

solution = Solution()
print(solution.isSymmetric(root))  # Output: True

# Creating a non-symmetric binary tree
root = Solution.TreeNode(1)
root.left = Solution.TreeNode(2)
root.right = Solution.TreeNode(2)
root.left.right = Solution.TreeNode(3)
root.right.right = Solution.TreeNode(3)

print(solution.isSymmetric(root))  # Output: False
