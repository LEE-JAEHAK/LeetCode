class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = a[::-1], b[::-1]
        sz = max(len(a),len(b))
        gap = len(a)-len(b) if len(a) > len(b) else len(b)-len(a)
        for i in range(gap):
            if len(a)<len(b): a += '0'
            else: b += '0'
        print(a,b)
        
        ans, sign = '', 0
        for i in range(sz):
            up = int(a[i]) + int(b[i]) + sign
            if up >= 2:
                 ans += str(up%2)
                 sign = 1
            else:
                ans += str(int(a[i]) + int(b[i]) + sign)
                sign = 0
        if sign == 1:
            ans += str(sign) 
        return ans[::-1]
        