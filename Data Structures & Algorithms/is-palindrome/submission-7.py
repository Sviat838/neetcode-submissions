class Solution:
    def isPalindrome(self, s: str) -> bool:

        left = 0
        right = len(s) - 1

        s = [e.lower() for e in s
            if ord('a') <= ord(e.lower()) <= ord('z') or ord('0') <= ord(e.lower()) <= ord('9')]

        median = len(s)//2

        for i in range(median):
            if s[i] != s[-i-1]:
                return False
            
            i+=1


        # while left < right:

        #     if not (ord('a') <= ord(s[left].lower()) <= ord('z') or ord('0') <= ord(s[left].lower()) <= ord('9')):
        #         left += 1
        #     elif not (ord('a') <= ord(s[right].lower()) <= ord('z') or ord('0') <= ord(s[right].lower()) <= ord('9')):
        #         right -= 1
        #     elif s[left].lower() == s[right].lower():
        #         left += 1
        #         right -= 1
        #     else:
        #         return False

        return True