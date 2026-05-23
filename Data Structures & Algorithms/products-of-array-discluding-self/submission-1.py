class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_sum = [1] * (len(nums))

        for i in range(0, len(nums)):
            prefix_sum[i] = prefix_sum[i - 1] * nums[i]

        res = []

        for i in range(-1, -len(nums)-1, -1):
            result: int = 1

            if i > -len(nums):
                result = prefix_sum[i-1]

            for y in range(i+1, 0, 1):
                result *= nums[y]

            res.insert(0, result)

        print(prefix_sum)
        print(res)
        return res

# 1) start from end, 1*2*4 = 8.  [0, 0, 0, 8]
# 2) 1 * 2 * 8 - 4 = 16**   [0, 0, 12, 8]
# 3) 1 * 12 * 2 = 24 [0, 24, 12 ,8]
# 4) 24 * 2 = 48


# inp [   1,      2,         4,       6]
# pre [   1,      2,         8,       48]

# res   inp[i+1:]      pre[-4]*inp[i+1:]       pre[-3]*inp[i+1:]          pre[-2]

# [ 2*4*6,  2*4*6, 8/4*6=12 ,  48/6=8]


# 2 * 4 * 6 = 48   {1}
# 48 =             {24}



