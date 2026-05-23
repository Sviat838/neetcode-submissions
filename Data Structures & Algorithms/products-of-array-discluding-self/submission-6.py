class Solution:
    def productExceptSelf(self, nums: List[int]):
        n = len(nums)
        pref = [1]*n
        suf = [1]*n

        res = [0] * n

        for i in range(n):
            pref[i] = nums[i] * pref[i-1]
        for i in range(-1, -n-1, -1):
            suf[i] = nums[i] * suf[i+1]

        for i in range(n):
            if i == 0:
                res[i] = suf[1]
            elif i == n-1:
                res[i] = pref[-2]
            else:
                res[i] = pref[i-1] * suf[i+1]

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



