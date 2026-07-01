class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # Track used digits in rows, columns, and 3x3 boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = []
        
        # Step 1: Initialize our tracking sets and record empty cell positions
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val != '.':
                    box_idx = (r // 3) * 3 + (c // 3)
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[box_idx].add(val)
                else:
                    empty_cells.append((r, c))
                    
        # Step 2: Backtracking function to try filling empty cells
        def backtrack(cell_idx=0):
            # If we've successfully filled all empty cells, we are done
            if cell_idx == len(empty_cells):
                return True
                
            r, c = empty_cells[cell_idx]
            box_idx = (r // 3) * 3 + (c // 3)
            
            # Try placing digits '1' through '9'
            for digit in map(str, range(1, 10)):
                if digit not in rows[r] and digit not in cols[c] and digit not in boxes[box_idx]:
                    # Place candidate digit
                    board[r][c] = digit
                    rows[r].add(digit)
                    cols[c].add(digit)
                    boxes[box_idx].add(digit)
                    
                    # Recursively proceed to the next cell
                    if backtrack(cell_idx + 1):
                        return True
                        
                    # Undo placement if it didn't lead to a valid solution (Backtrack)
                    board[r][c] = '.'
                    rows[r].remove(digit)
                    cols[c].remove(digit)
                    boxes[box_idx].remove(digit)
                    
            return False

        backtrack()