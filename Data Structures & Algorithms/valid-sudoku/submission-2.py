class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        column_dict = collections.defaultdict(set)
        row_dict = collections.defaultdict(set)
        squares = collections.defaultdict(set)
        for row in range(len(board)):
            for col in range(len(board[row])):
                value = board[row][col]
                if value == '.':
                    continue
                if value in row_dict[row] or value in column_dict[col] or value in squares[(row//3,col//3)]:
                    return False
                
                column_dict[col].add(value)
                row_dict[row].add(value)
                squares[(row//3,col//3)].add(value)
        return True