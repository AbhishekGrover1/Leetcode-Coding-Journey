class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        # Initialize an n x n matrix with zeros
        matrix = [[0] * n for _ in range(n)]
        
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        num = 1
        
        while top <= bottom and left <= right:
            # 1. Traverse from left to right across the top row
            for c in range(left, right + 1):
                matrix[top][c] = num
                num += 1
            top += 1
            
            # 2. Traverse from top to bottom down the right column
            for r in range(top, bottom + 1):
                matrix[r][right] = num
                num += 1
            right -= 1
            
            # 3. Traverse from right to left across the bottom row
            for c in range(right, left - 1, -1):
                matrix[bottom][c] = num
                num += 1
            bottom -= 1
            
            # 4. Traverse from bottom to top up the left column
            for r in range(bottom, top - 1, -1):
                matrix[r][left] = num
                num += 1
            left += 1
            
        return matrix