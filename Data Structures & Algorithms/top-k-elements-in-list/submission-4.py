class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = defaultdict(int)

        result_list = []

        for e in nums:
            result[e] += 1

        # for kk, v in result.items():
        #     if not result_list:
        #         result_list.append(kk)
        #     elif result[result_list[0]] <= v:
        #         result_list.insert(0, kk)
        #     else:
        #         result_list.append(kk)
        #
        # print(result)

        return [x[0] for x in sorted(result.items(), key=lambda x: x[1], reverse=True)[:k]]