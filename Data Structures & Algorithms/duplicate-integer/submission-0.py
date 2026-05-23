class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        old = None

        for el in nums:
            
            if old is None:
                old = el
                continue

            if old == el:
                return True
            
            old = el

        return False


