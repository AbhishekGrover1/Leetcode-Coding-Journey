class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        
        stack, res = [root], []
        
        while stack:
            node = stack.pop()
            res.append(node.val)
            
            # Push left first so right is processed next
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
                
        return res[::-1]