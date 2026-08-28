class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(len(board)): # or range(9)
            
            seen_row = set()
            for r in range(len(board[i])): # or range(9)
                if board[i][r] == ".":
                    continue
                print(board[r])
                if board[i][r] in seen_row:
                    return False
                seen_row.add(board[i][r])
                
            seen_col = set()
            for c in range(len(board)):
                if board[c][i] == ".":
                    continue
                print(board[c][i])
                if board[c][i] in seen_col:
                    return False
                seen_col.add(board[c][i])
                
            seen_square = set()
            for i in range(0, 9, 3):
                for j in range(0, 9, 3): 
                    seen_square = set() 
                    
                    for r in range(i, i + 3): 
                        for c in range(j, j + 3): 
                            if board[r][c] == ".": 
                                continue 
                            if board[r][c] in seen_square: 
                                return False 
                            
                            seen_square.add(board[r][c])

        return True 