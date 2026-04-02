class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW = len(matrix)
        COL = len(matrix[0])
        row = 0
        # find row
        while row < ROW:
            rm = matrix[row][-1]
            if target < rm:
                for i in range(COL):
                    if matrix[row][i] == target:
                        return True
                return False
            elif target > rm:
                row+=1
            else:
                return True
        return False