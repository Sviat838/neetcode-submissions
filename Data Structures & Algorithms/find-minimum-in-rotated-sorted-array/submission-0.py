class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 3 4 5 6 1 2
        r = len(nums)-1
        l = 0

        res = 999

        while l <= r:
            print('l: ' + str(l), "; r: " + str(r))
            if nums[l] < nums[r]:
                r -= 1
            elif nums[l] > nums[r]:
                l += 1
            elif nums[l] < nums[r]:
                r -= 1
            elif l == r:
                res = nums[l]
                l += 1

        return res
