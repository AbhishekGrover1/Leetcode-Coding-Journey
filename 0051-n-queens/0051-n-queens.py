class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        result = []
        
        # Tracking sets to identify columns and diagonals under attack
        cols = set()
        pos_diag = set() # (r + c)
        neg_diag = set() # (r - c)
        
        # Initialize an empty board configuration
        board = [["."] * n for _ in range(n)]
        
        def backtrack(r):
            # Base Case: If we successfully placed queens in all rows (0 to n-1)
            if r == n:
                # Format the board grid into strings for the final output
                copy = ["".join(row) for row in board]
                result.append(copy)
                return
            
            # Attempt to place a queen in each column of the current row 'r'
            for c in range(n):
                # If the column or either diagonal is under attack, skip this cell
                if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue
                
                # Make choice: Place the queen
                cols.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                board[r][c] = "Q"
                
                # Recursively move to the next row
                backtrack(r + 1)
                
                # Undo choice (Backtrack)
                cols.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                board[r][c] = "."
                
        backtrack(0)
        return result