class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        neg_flag = plus_flag = ret_str = ''
        str = str.strip()
        
        if str == '':
            return 0
        
        if len(str) == 1 and ('-' in str[0] or '+' in str[0]):
            return 0
        
        if '-' in str[0]:
            neg_flag = '-'
            str = str[1:]
        elif '+' in str[0]:
            plus_flag = '+'
            str=str[1:]
            
        if not str[0].isdigit():
            return 0
        
        for c in str:
            if c.isdigit():
                ret_str += c
            else:
                break
        
        ret_str = neg_flag + plus_flag + ret_str
        ret_str = int(ret_str)
        
        if ret_str < -2147483648: return -2147483648
        elif ret_str > 2147483647: return 2147483647
        return ret_str
            