class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        res = [0] * len(temp)

        for i in range(len(temp)):
            j = i + 1

            while j < len(temp):
                if temp[j] > temp[i]:
                    res[i] = j - i
                    break
                
                j += 1
        
        return res
