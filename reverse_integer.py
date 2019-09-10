'''
https://leetcode.com/problems/reverse-integer/
'''

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        str_x = str(x)
        len_x = len(str_x)
        ret_str = ''
        
        
        for index in reversed(range(len_x)):
            ret_str = ret_str + str_x[index]
        
        if '-' in ret_str:
            ret_str = '-' + ret_str[:-1]
        ret_str = int(ret_str)
        
        if(abs(ret_str) > (2 ** 31 - 1)):
            return 0
        else:
            return(ret_str)
            
Class Solution2(object):
    def reverse2(self, x):
        """
        :type x: int
        :rtype: int
        """
        str_x = str(x)
        len_x = len(str_x)
        ret_str = str(x)[::-1]
                
        if x < 0:
            ret_str = '-' + ret_str[:-1]
            
        ret_rev = int(ret_str)
            
        if(abs(ret_rev) > (2 ** 31 - 1)):
            return 0
        else:
            return(ret_rev)