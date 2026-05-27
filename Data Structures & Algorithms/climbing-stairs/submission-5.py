class Solution:
    def climbStairs(self, n: int, prev = []) -> int:
        # * * * * 
        # 1 + 1 + 1 + 1 + 1
        # 2 + 1 + 1 + 1
        # 1 + 2 + 1 + 1
        # 1 + 1 + 2 + 1
        # 1 + 1 + 1 + 2
        # 2 + 2 + 1
        # 1 + 2 + 2
        # 2 + 1 + 2

        # 1 2 3 4 5

        prev = [0,1]

        for i in range(1,n+1):
            prev.append(prev[-2] + prev[-1])

        return prev[-1]


        # 1 = 1
        # 2 = 2
        # 3 = 3
        # 4 = 5
        # 5 = 8