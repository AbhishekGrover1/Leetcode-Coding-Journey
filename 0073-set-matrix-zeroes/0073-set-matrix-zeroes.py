class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
            
        m, n = len(matrix), len(matrix[0])
        first_col_zero = False
        
        # 1. Scan the matrix and use the first row/col as markers
        for i in range(m):
            # Check if the first column needs to be zeroed out later
            if matrix[i][0] == 0:
                first_col_zero = True
                
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0  # Mark its row
                    matrix[0][j] = 0  # Mark its column
                    
        # 2. Iterate backwards (or skip first row/col) to update cells based on flags
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, 0, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
                    
            # Update the first column cell if needed
            if first_col_zero:
                matrix[i][0] = 0