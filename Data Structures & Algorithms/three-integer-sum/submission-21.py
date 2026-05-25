class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        res = []

        for i, e in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums)-1

            while l < r:

                three_sum = e + nums[l] + nums[r]

                if three_sum < 0:
                    l += 1

                elif three_sum > 0:
                    r -= 1

                elif three_sum == 0:
                    res.append([e, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l]==nums[l-1]:
                        l += 1


        return res
