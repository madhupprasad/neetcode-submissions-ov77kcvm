class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW = len(matrix)
        COL = len(matrix[0])
        l = 0
        r = ROW * COL -1

        while l <= r:
            m = (l + r)//2
            row = m//COL
            col = m%COL
            if target > matrix[row][col]:
                l = m + 1
            elif target < matrix[row][col]:
                r = m - 1
            else:
                return True
        return False
