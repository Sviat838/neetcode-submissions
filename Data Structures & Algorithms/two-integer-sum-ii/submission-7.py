class Solution:
    def twoSum(self, n: List[int], t: int) -> List[int]:

        # [1,2,3,4]
        #  *     *
        #  *   *
        #  * *
 
        left = 0
        right = len(n)-1

        res = []

        while left < right:
            if n[left] + n[right] == t:
                return [left+1, right+1]
            elif n[left] + n[right] > t:
                right -= 1
            elif n[left] + n[right] < t:
                left += 1

        return []
