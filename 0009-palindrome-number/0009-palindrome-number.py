class Solution(object):
    def isPalindrome(self, x):
        tmp = str(x)
        tmp2 = tmp[::-1]
        return tmp == tmp2
        """
        :type x: int
        :rtype: bool
        """