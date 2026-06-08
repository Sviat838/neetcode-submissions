class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        max_len = 1
        
        w = [s[0]]

        l = 0
        r = 1

        while r < len(s):
            if s[r] not in w:
                w.append(s[r])
                r += 1
                max_len = max(max_len, len(w))
            else:
                l += 1
                r = l+1
                w = [s[l]]


        return max_len