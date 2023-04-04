class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a, b, sign= 0, 0, False
        for i in reversed(range(len(s))):
            if s[i].isalpha() and not sign:
                sign = True
                a = i
            if sign:
                if s[i] == ' ':
                    b = i + 1
                    break
        return (a - b + 1)