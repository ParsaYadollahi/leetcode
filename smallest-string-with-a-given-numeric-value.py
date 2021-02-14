'''
  smallest-string-with-a-given-numeric-value
  TLE AGAIN....
'''


class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        output = ['a'] * n

        for i in range(n-1, -1, -1):
            if (sum(output) + 25 < k):
                output[i] = 26
            else:
                x = 26
                while(sum(output) + x - 1 > k):
                    x -= 1
                output[i] = x

        ret = ''
        for i in range(len(output)):
            ret += chr(output[i] + 96)

        return ret


class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        output = ['a'] * n
        tot = n
        for i in range(n-1, -1, -1):
            if tot < k:
                output[i] = chr(min(ord('z'), (k-tot)+ord('a')))
                tot += ord(output[i]) - ord('a')

            if tot == k:
                break
        return ''.join(output)
