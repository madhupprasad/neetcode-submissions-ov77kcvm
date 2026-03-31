class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        1. Find the row in which the element might be there
        2. Normal Binary search
        """

        rows = len(matrix)
        cols = len(matrix[0])

        # find row
        left = 0
        right = rows-1

        while left <= right:
            mid = (left + right)//2
            if target > matrix[mid][-1]:
                left = mid + 1
            elif target < matrix[mid][0]:
                right = mid - 1
            else:
                break
        row = (left + right)//2
        left = 0
        right = cols-1
        while left <= right:
            mid = (left + right)//2
            if target > matrix[row][mid]:
                left = mid + 1
            elif target < matrix[row][mid]:
                right = mid - 1
            else:
                return True

        return False
