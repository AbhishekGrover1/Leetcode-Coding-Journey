# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[Optional[TreeNode]]
        """
        if n == 0:
            return []
            
        def build_trees(start, end):
            # Base case: if start > end, no subtree can be formed (return None)
            if start > end:
                return [None]
                
            all_trees = []
            
            # Consider each number in the range as a potential root
            for i in range(start, end + 1):
                # Generate all possible left and right subtrees
                left_trees = build_trees(start, i - 1)
                right_trees = build_trees(i + 1, end)
                
                # Connect the root 'i' with all combinations of left and right subtrees
                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        all_trees.append(root)
                        
            return all_trees

        return build_trees(1, n)