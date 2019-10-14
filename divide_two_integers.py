class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # 3k dislikes cuz of time limit. Still take this as correct
        dividend_flag = divisor_flag = False
        counter = 0
        if divisor < 0:
            divisor_flag = True
        if dividend < 0:
            dividend_flag = True

        dividend = abs(dividend)
        divisor = abs(divisor)

        while(dividend-divisor >= 0):
            dividend -= divisor
            counter += 1
        
        if dividend_flag ^ divisor_flag:
            counter = -counter
        return counter