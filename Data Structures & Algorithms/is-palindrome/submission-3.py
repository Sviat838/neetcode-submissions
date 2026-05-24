class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().replace(' ', '')
        ss = ''

        for e in s:
            if ord('a') <= ord(e) <= ord('z') or ord('0') <= ord(e) <= ord('9'):
                ss += e

        reversed_s = ''.join(
            [ss[i] for i in range(-1, -len(ss) - 1, -1)]
        )

        return ss == reversed_s