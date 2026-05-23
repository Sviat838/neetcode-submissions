class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = defaultdict(int)

        result_list = []

        for e in nums:
            result[e] += 1

        # return [x[0] for x in sorted(result.items(), key=lambda x: x[1], reverse=True)[:k]]

        reversed_dict = dict[int, list]()
        for kk, v in result.items():
            if not v in reversed_dict:
                reversed_dict[v] = [kk]
            elif v in reversed_dict:
                reversed_dict[v] += [kk]

        for kk in sorted(reversed_dict.keys(), reverse=True):
            result_list += reversed_dict[kk]
            if len(result_list) == k:
                return result_list

        return result_list[:k]