class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sub_box = defaultdict(set)
        for i in range(9):
            seen_in_this_row = set()
            seen_in_this_column = set()
            for j in range(9):
                if board[i][j] in seen_in_this_row and board[i][j] != ".":
                    return False
                if board[j][i] in seen_in_this_column and board[j][i] != ".":
                    return False

                seen_in_this_row.add(board[i][j])
                seen_in_this_column.add(board[j][i])
                origin = i - (i % 3), j - (j % 3)
                if board[i][j] in sub_box[origin] and board[i][j] != ".":
                    return False
                sub_box[origin].add(board[i][j])
        return True