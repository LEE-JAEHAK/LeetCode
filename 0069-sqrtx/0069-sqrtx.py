class Solution:
    def mySqrt(self, x: int) -> int:
        for i in range(2**16):
            if i**2 > x:
                return (i - 1)
                