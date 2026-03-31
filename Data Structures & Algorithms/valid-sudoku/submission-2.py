class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = []
        cols = []
        box = []

        bmap = {
            (0, 0): 0,
            (0, 1): 1,
            (0, 2): 2,
            (1, 0): 3,
            (1, 1): 4,
            (1, 2): 5,
            (2, 0): 6,
            (2, 1): 7,
            (2, 2): 8,
        }

        for _ in range(9):
            rows.append(set())
            cols.append(set())
            box.append(set())
        
        for i in range(9):
            for j in range(9):
                v = board[i][j]
                if v == ".":
                    continue
                if v not in rows[i]:
                    rows[i].add(v)
                else:
                    return False
                if v not in cols[j]:
                    cols[j].add(v)
                else:
                    return False
                if v not in box[bmap[(i//3,j//3)]]:
                    box[bmap[(i//3,j//3)]].add(v)
                else:
                    return False
        
        return True
        
