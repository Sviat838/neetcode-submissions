class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        res = [0] * len(temp)

        s = []

        for i in range(len(temp)):
            
            while s and temp[i] > temp[s[-1]]:
                last_index = s.pop()
                res[last_index] = i - last_index
                
                
            s.append(i)
            



        
        return res
