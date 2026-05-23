class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = [0]*26
        l = [0]*26

        if len(s) != len(t):
            return False

        counter = 0

        for i in range(len(s)):
            d1[ord(s[i]) - ord('a')] += 1
            d1[ord(t[i]) - ord('a')] -= 1

        return d1 == [0]*26