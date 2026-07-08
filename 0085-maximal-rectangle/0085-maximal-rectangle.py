class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        
        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0
        
        for row in matrix:
            for col in range(cols):
                # Update the height of the histogram for the current row
                if row[col] == '1':
                    heights[col] += 1
                else:
                    heights[col] = 0
            
            # Calculate max rectangle area for the current row's histogram
            max_area = max(max_area, self.largestRectangleArea(heights))
            
        return max_area

    def largestRectangleArea(self, heights):
        stack = []  # Pairs of (index, height)
        max_area = 0
        
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                max_area = max(max_area, height * (i - idx))
                start = idx
            stack.append((start, h))
            
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
            
        return max_area