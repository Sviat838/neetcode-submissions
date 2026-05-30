class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        l1, l2 = 0, 0

        for i in range(1, len(position)):
            index = i - 1
            while index >= 0 and position[index] > position[i]:
                position[index], position[i] = position[i], position[index]
                speed[index], speed[i] = speed[i], speed[index]
                i -= 1
                index -= 1

        res = [0] * len(position)
        # 
        for i in range(len(position)):
            res[i] = (target - position[i]) / speed[i]

        res_group = []
        i = len(res) - 1
        while i >= 0:
            lead_time = res[i]
            res_group.append(lead_time)
            i -= 1
            while i >= 0 and res[i] <= lead_time:
                i -= 1


        return len(res_group)