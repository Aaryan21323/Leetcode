# brute force method 
class Solution1:
    def isValidSudoku(self,board:list[list[str]])->bool:
        for row in board:
            row_set=set()
            for cell in row:
                if cell!=".":
                    if cell in row_set:
                        return False
                    else:
                        row_set.add(cell)
        for i in range(len(board)):
            col_set=set()
            for cell in board:
                if cell[i]!=".":
                    return False
                else:
                    col_set.add(cell[i])
        for row in range(3):
            for col in range(3):
                box=set()
                for r in range(row*3,row*3+3):
                    for c in range(col*3,col*3+3):
                        cell=board[r][c]
                        if cell!=".":
                            if cell in box:
                                return False
                            else:
                                box.add(cell)
        return True
    
# neetcode 

class Solution:
    def isValidSudoku(self,board=list[list[str]])->bool:
        cols={}
        rows={}
        squares={}

        for r in range(9):
            for c in range(9):
                if board[r][c]==".":
                    continue
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares((r//3,c//3))):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])
        return True


# set method

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                num = board[r][c]
                square_index = (r // 3) * 3 + (c // 3)

                if (num in rows[r] or
                    num in cols[c] or
                    num in squares[square_index]):
                    return False

                rows[r].add(num)
                cols[c].add(num)
                squares[square_index].add(num)

        return True