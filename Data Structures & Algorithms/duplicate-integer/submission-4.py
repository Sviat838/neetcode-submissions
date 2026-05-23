class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        if len(nums) == 1:
            return False

        for i in range(0, len(nums), 2):
            if i+1 >= len(nums):
                return nums[i] == nums[i-1]
            elif nums[i] == nums[i+1]:
                return True

        return False
