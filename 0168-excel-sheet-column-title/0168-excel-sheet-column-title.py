class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        a = columnNumber
        st = ''
        while a > 0:
            st += chr((a-1)%26 + 65)
            a = (a-1) // 26
        return (st[::-1])