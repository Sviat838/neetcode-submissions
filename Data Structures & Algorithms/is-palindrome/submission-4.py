class Solution:
    def isPalindrome(self, s: str) -> bool:

        left = 0
        right = len(s) - 1


        while left < right:

            if not (ord('a') <= ord(s[left].lower()) <= ord('z') or ord('0') <= ord(s[left].lower()) <= ord('9')):
                left += 1
            elif not (ord('a') <= ord(s[right].lower()) <= ord('z') or ord('0') <= ord(s[right].lower()) <= ord('9')):
                right -= 1
            elif s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False

        return True