class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ''
        for i in s:
            if not (i.isalpha() or i.isnumeric()):
                continue
            res += i
        res = res.lower()
        # a = list(res)
        # return a == list(reversed(a))
        return res == res[::-1]