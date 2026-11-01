class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rowMap = defaultdict(set)
        colMap = defaultdict(set)
        squares = defaultdict(set)

        for row in range(9):
            for cols in range(9):
                if board[row][cols] == '.':
                    continue
                
                if (board[row][cols] in rowMap[row]
                    or board[row][cols] in colMap[cols]
                    or board[row][cols] in squares[(row // 3,cols // 3)]):
                    return False
                
                rowMap[row].add(board[row][cols])
                colMap[cols].add(board[row][cols])
                squares[(row // 3, cols // 3)].add(board[row][cols])
        return True
                
            
        