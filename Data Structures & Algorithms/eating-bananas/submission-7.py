class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = 1

        res = None

        len_piles = len(piles)

        l = 1
        r = max(piles)
        
        while l <= r:
            median = (r+l)//2

            total_hours = None
            pils_turns = []

            for i in range(len_piles):
                pils_turns.append(math.ceil(piles[i]/median))

            total_hours = sum(pils_turns)

            if total_hours <= h:
                res = median
                r = median - 1
            elif total_hours > h:
                l = median + 1
        
        return res
