class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
            
        # If the node is a leaf, its depth is 1
        if not root.left and not root.right:
            return 1
            
        # If the left child is missing, the shortest path must be on the right
        if not root.left:
            return self.minDepth(root.right) + 1
            
        # If the right child is missing, the shortest path must be on the left
        if not root.right:
            return self.minDepth(root.left) + 1
            
        # If both children exist, return the minimum of the two subtrees
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1