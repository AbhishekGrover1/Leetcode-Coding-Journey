class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
            
        m, n = len(matrix), len(matrix[0])
        low, high = 0, (m * n) - 1
        
        while low <= high:
            mid = (low + high) // 2
            # Map the 1D index back to 2D matrix coordinates
            mid_element = matrix[mid // n][mid % n]
            
            if mid_element == target:
                return True
            elif mid_element < target:
                low = mid + 1
            else:
                high = mid - 1
                
        return False