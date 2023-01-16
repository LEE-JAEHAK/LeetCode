class Solution(object):
    def romanToInt(self, s):
        sum = 0
        list = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        for i in range(len(s)):
            if i < len(s)-1 and list[s[i]] < list[s[i+1]]:
                sum -= list[s[i]]
            else:
                sum += list[s[i]]
        return sum
                
            
        """
        :type s: str
        :rtype: int
        """
        