class Solution(object):
    def isValid(self, s):
        stack = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                tmp = stack.pop()
                if tmp == '(' and i != ')':
                    return False
                if tmp == '[' and i != ']':
                    return False
                if tmp == '{' and i != '}':
                    return False
        if len(stack) != 0:
            return False
        return True
            
        """
        :type s: str
        :rtype: bool
        """
        