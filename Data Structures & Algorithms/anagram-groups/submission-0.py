class Solution:
    def is_anagram(self, str1, str2):
            l = {}

            if len(str1) != len(str2):
                return False

            for i in range(len(str1)):
                l[str1[i]] = l.get(str1[i], 0) + 1
                l[str2[i]] = l.get(str2[i], 0) - 1

                if l[str1[i]] == 0:
                    del l[str1[i]]
                if str2[i] in l and  l[str2[i]] == 0:
                    del l[str2[i]]

            return l == {}

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







