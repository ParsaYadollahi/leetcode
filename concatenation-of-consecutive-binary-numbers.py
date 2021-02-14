'''
  https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/
  time limit exceeded, but the second one is fine, huh?
'''


class Solution:
    def concatenatedBinary(self, n: int) -> int:
        output = ''
        for i in range(1, n+1):
            output += self.binary_converter(i)

        return self.decimal_to_binary(output)

    def decimal_to_binary(self, n):
        output = 0
        temp = int(n)
        base = 0
        while(temp):

            last_digit = temp % 10
            temp = temp//10
            output += last_digit * (2**base)
            base += 1
        return output % (10**9 + 7)

    def binary_converter(self, n):
        output = ''
        while (n > 0):
            rem = n % 2
            n //= 2
            output += str(rem)
        return output[::-1]


class Solution:
    def concatenatedBinary(self, n: int) -> int:
        res = ''

        for i in range(1, n+1):
            res += bin(i)[2:]

        return int(res, 2) % (10**9 + 7)
