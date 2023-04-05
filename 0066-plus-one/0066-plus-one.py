class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        a, b = '', ''
        for i in digits:
            a += str(i)
        b = int(a) + 1
        return (list(map(int, str(b))))