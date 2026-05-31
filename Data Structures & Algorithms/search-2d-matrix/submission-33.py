class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = []

        top = 0
        bot = len(matrix) - 1

        median = 0

        while top <= bot:
            median = (bot + top) // 2 if top != bot else top

            if matrix[median][0] < target and matrix[median][-1] < target:
                top = median+1
            elif matrix[median][0] > target and matrix[median][-1] > target:
                bot = median-1
            else:
                break

        row = matrix[median]

        left = 0
        right = len(row)-1

        print(row)

        while left <= right:
            median = (right + left) // 2
            if left == right:
                return row[median] == target
            elif row[median] == target:
                return True
            elif row[median] > target:
                right = median - 1
            else:
                left = median + 1

        return False