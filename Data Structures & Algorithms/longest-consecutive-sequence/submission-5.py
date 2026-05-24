class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))

        counter = 1
        counter_res = [0 if not nums else 1]

        for e in range(1, len(nums)):
            if nums[e] - nums[e - 1] == 1:
                counter += 1
            elif (nums[e] - nums[e - 1] != 1) or e == len(nums) - 1:
                counter_res.append(counter)
                counter = 1

            if e == len(nums) - 1:
                counter_res.append(counter)

        return max(counter_res)