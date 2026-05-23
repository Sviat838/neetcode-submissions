class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)

        pointer = 0

        for i in range(1, len(nums)):

            while pointer < i and sorted_nums[i] + sorted_nums[pointer] <= target:

                if sorted_nums[i] + sorted_nums[pointer] == target:

                    index1 = nums.index(sorted_nums[pointer])
                    index2 = nums.index(sorted_nums[i])
                    
                    if index2 == index1:
                        deleted_val = sorted_nums[pointer]

                        nums.remove(sorted_nums[pointer])

                        if deleted_val <= sorted_nums[i]:
                            index1 = nums.index(sorted_nums[i]) + 1
                        else:
                            index1 = nums.index(sorted_nums[i])

                    return sorted([index1, index2])
                
                pointer += 1
            
            pointer = 0

        return []
            


# 2,4,7,8 -> 11
# 8,4,7,2

        return []