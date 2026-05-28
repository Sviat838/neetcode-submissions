class Solution:

    def insertionSort(self,  pairs: List[Pair]) -> List[List[Pair]]:

        res = []
        for i in range(len(pairs)):
            j = i
            # Inner loop: move the element at j left until it's in the right spot
            while j > 0 and pairs[j-1].key > pairs[j].key:
                pairs[j], pairs[j-1] = pairs[j-1], pairs[j]
                j -= 1
            
            # Take a snapshot of the array after the ith element is 'inserted'
            res.append(list(pairs))

        return res
