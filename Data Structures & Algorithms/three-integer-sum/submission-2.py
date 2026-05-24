class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        res = set()

        for i in range(2, len(nums)):
            for j in range(1,i):
                if nums[i] + nums[j] + nums[0] > 0:
                    continue
                for k in range(j):
                    if nums[i] + nums[j] + nums[k] == 0:
                        res.add((nums[i], nums[j], nums[k]))

        return list(list(e) for e in res)