class Solution(object):
    def longestCommonPrefix(self, strs):
        v = sorted(strs)
        ans = ''
        for i in range(min(len(v[0]), len(v[-1]))):
            if v[0][i] == v[-1][i]:
                ans += v[0][i]
            else:
                break
        return ans
        """
        :type strs: List[str]
        :rtype: str
        """