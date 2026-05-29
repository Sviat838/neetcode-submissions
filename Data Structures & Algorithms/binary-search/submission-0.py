class Solution:
    def search(self, arr, target):
        left = 0
        right = len(arr) - 1

        while left <= right:
            median = (left + right) // 2

            if arr[median] == target:
                return median
            elif arr[median] > target:
                right = median - 1
            elif arr[median] < target:
                left = median + 1


        return -1
        