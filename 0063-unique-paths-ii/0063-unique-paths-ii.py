class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0
            
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        # Initialize a 1D DP array for the current row
        dp = [0] * n
        dp[0] = 1 # Starting point
        
        for r in range(m):
            for c in range(n):
                if obstacleGrid[r][c] == 1:
                    dp[c] = 0
                elif c > 0:
                    # dp[c] currently holds the value from the row above
                    # dp[c-1] holds the value from the left cell
                    dp[c] += dp[c - 1]
                    
        return dp[-1]