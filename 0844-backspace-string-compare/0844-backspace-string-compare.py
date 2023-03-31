class Solution(object):
    def backspaceCompare(self, s, t):
        st1 = []
        st2 = []
        for i in s:
            if i != '#':
                st1.append(i)
            else:
                if st1:
                    st1.pop()
        for i in t:
            if i != '#':
                st2.append(i)
            else:
                if st2:
                    st2.pop()
        return st1 == st2
        
                
        """
        :type s: str
        :type t: str
        :rtype: bool
        """