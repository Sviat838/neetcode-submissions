class Solution:
    def threeSum(self, n: List[int]) -> List[List[int]]:
        res = set()

        n = sorted(n)

        r = len(n) - 1
        for i in range(len(n)):
            m = i+1
            r = len(n) - 1

            while m < r:
                # if i > 0 and n[i] == n[i-1]:
                #     l+=1
                #     break

                if n[i] + n[m] + n[r] > 0:
                    r -= 1

                elif n[i] + n[m] + n[r] < 0:
                    m += 1

                elif n[i] + n[m] + n[r] == 0:
                    res.add(tuple(sorted([n[i], n[m], n[r]])))
                    m+=1

        return [list(s) for s in res]