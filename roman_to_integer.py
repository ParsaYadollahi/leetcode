class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbol = {
            'M' : 1000,
            'D' : 500,
            'C' : 100,
            'L' : 50,
            'X' : 10,
            'I' : 1,
            'V' : 5,
        }
        sum = 0
        if 'IV' in s:
            s = s.replace('IV', '')
            sum += 4
        if 'IX' in s:
            s = s.replace('IX', '')
            sum += 9
        if 'XL' in s:
            s = s.replace('XL', '')
            sum += 40
        if 'XC' in s:
            s = s.replace('XC', '')
            sum += 90
        if 'CD' in s:
            s = s.replace('CD', '')
            sum += 400
        if 'CM' in s:
            s = s.replace('CM', '')
            sum += 900
        
        for i in s:
            sum += symbol[i]

        return sum

