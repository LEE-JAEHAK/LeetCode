class Solution(object):
    def calculate(self, s):
        st = []
        cur = 0
        sign = 1
        total = 0
        for i in s:
            if i.isdigit():
                cur *= 10
                cur += int(i)
            elif i == '+':
                total += cur * sign                
                sign, cur = 1, 0
            elif i == '-':
                total += cur * sign
                sign, cur = -1, 0
            elif i == '(':
                st.append(total)
                st.append(sign)
                total, sign = 0, 1
            elif i == ')':
                total += cur * sign
                sign, cur = 1, 0
                total *= st.pop()
                total += st.pop()
        if cur:total += cur * sign
        return total