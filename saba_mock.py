'''
  https://leetcode.com/problems/plus-one
'''


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        len_arr = len(digits)
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            temp = digits[i] + carry
            digits[i] = temp % 10
            carry = temp//10

            if carry == 0:
                return digits

        return [1] + digits
