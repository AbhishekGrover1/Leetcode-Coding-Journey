# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True
        
        return self.isMirror(root.left, root.right)
    
    def isMirror(self, t1, t2):
        # If both nodes are None, they are symmetric mirrors
        if not t1 and not t2:
            return True
        # If only one is None, they cannot be mirrors
        if not t1 or not t2:
            return False
        
        # Check if current values match, and cross-compare their subtrees
        return (t1.val == t2.val and 
                self.isMirror(t1.left, t2.right) and 
                self.isMirror(t1.right, t2.left))