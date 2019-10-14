'''
https://leetcode.com/problems/generate-parentheses/
'''
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        ans = []
        def gen_par(s = '', l = 0, r = 0):
            if len(s) == 2*n:
                ans.append(s)
                return
            # turns out the more you try to understand the solution
            # the more you memorize it....
            
            if l < n:
                gen_par(s+'(', l+1, r)
            if r < l:
                gen_par(s+')', l, r+1)

        gen_par()
        return ans
