# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        def build_bst(left, right):
            # Base case: if the left pointer crosses the right, we are done
            if left > right:
                return None
            
            # Find the middle index
            mid = (left + right) // 2
            
            # Create the root node with the middle element
            root = TreeNode(nums[mid])
            
            # Recursively build the left and right subtrees
            root.left = build_bst(left, mid - 1)
            root.right = build_bst(mid + 1, right)
            
            return root
        
        # Initialize the recursion with the full array bounds
        return build_bst(0, len(nums) - 1)