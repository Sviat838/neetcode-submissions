class Solution:
    def threeSum(self, n: List[int]) -> List[List[int]]:
        res = []

        n = sorted(n)

        r = len(n) - 1
        for i in range(len(n)):
            m = i+1
            r = len(n) - 1

            if n[i] > 0:
                break

            if n[i] == n[i-1] and i > 0:
                continue

            while m < r:

                if n[i] + n[m] + n[r] > 0:
                    r -= 1

                elif n[i] + n[m] + n[r] < 0:
                    m += 1

                elif n[i] + n[m] + n[r] == 0:
                    res.append([n[i], n[m], n[r]])
                    m+=1
                    while m < r and n[m] == n[m - 1]:
                        m += 1

        return res