class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = []

        top = 0
        bot = len(matrix) - 1

        median = 0

        while top <= bot:
            median = (bot + top) // 2 if top != bot else top

            if matrix[median][0] == target or matrix[median][-1] == target:
                return True
            elif bot == top:
                break
            elif top == bot and (matrix[median][0] < target or matrix[median][-1] < target):
                return False
            # elif len(matrix) == 1 and matrix[median][0] != target:
            #     median = 0
            #     top += 1
            elif (matrix[median][0] < target < matrix[median][-1]):
                break
            elif matrix[median][0] < target and matrix[median][-1] < target:
                top = median+1
            elif matrix[median][0] > target and matrix[median][-1] > target:
                bot = median

        # for i in range(len(matrix)):
        #     if matrix[i][0] > target:
        #         row = matrix[i]
        #     elif matrix[i][0] == target:
        #         return True

        row = matrix[median]

        left = 0
        right = len(row)-1

        print(row)

        while left <= right:
            # print(median)
            median = (right + left) // 2
            if left == right:
                return row[median] == target
            elif row[median] == target:
                return True
            elif row[median] > target:
                right = median
            else:
                left = median + 1

        return False