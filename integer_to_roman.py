'''
https://leetcode.com/problems/integer-to-roman/
'''

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        value = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        symbol = ['M', 'CM','D', 'CD', 'C', 'XC', 'L', 'XL', 
                                'X', 'IX', 'V', 'IV', 'I']
        ret_str = ''

        for i in range(len(value)):
            occurence = num / value[i]
            ret_str = ret_str + symbol[i]*occurence
            num = num%value[i]
        return ret_str

        
