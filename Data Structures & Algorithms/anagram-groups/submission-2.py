class Solution:
    def is_anagram(self, str1, str2):

            if len(str1) != len(str2):
                return False

            return Counter(str1) == Counter(str2)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = dict[str, list]()

        result[strs[0]] = [strs[0]]
        strs.pop(0)
        

        for s in strs:
            match_found = False
            for k in result:

                if self.is_anagram(s, k):
                    result[k].append(s)
                    match_found = True
            
            if not match_found:
                result[s] = [s]

        return list(result.values())







