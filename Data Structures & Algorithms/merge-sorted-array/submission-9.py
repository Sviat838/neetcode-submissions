class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # median = len()

        i1 = m-1
        i2 = n-1

        res_i = m+n-1

        while m > 0 and n > 0:

            if nums1[m-1] >= nums2[n-1]:
                nums1[res_i] = nums1[m-1]
                m-=1
            
            elif nums1[m-1] < nums2[n-1]:
                nums1[res_i] = nums2[n-1]
                n-=1
            res_i -= 1

        while n > 0:
            nums1[res_i] = nums2[n - 1]
            n -= 1
            res_i -= 1
    #      *             *
    # [1 3 5 0 0]    [2, 8]
    #      *          *
    # [1 3 5 5 8].   [2, 8]