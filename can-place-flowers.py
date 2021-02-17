'''
  https://leetcode.com/problems/can-place-flowers
  this one question gave me so much anxiety... took me too long to do
'''


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        for i in range(len(flowerbed)):
            if (
                (flowerbed[i] == 0) and
                (i == 0 or flowerbed[i-1] == 0) and
                (i == len(flowerbed)-1 or flowerbed[i+1] == 0)
            ):

                flowerbed[i] = 1
                n -= 1

            if n <= 0:
                return True

        return False
