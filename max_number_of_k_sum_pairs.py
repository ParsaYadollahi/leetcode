'''
  https://leetcode.com/problems/max-number-of-k-sum-pairs/
  First run got time limit exceeded. Then all downhill from there.... got help from online
'''


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        dict = {}
        output = 0

        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict.setdefault(num, 1)

            target = k - num
            if target in dict:
                if num != target:
                    if dict[num] > 0 and dict[target] > 0:
                        dict[num] -= 1
                        dict[target] -= 1
                        output += 1
                elif dict[num] >= 2:
                    dict[num] -= 2
                    output += 1

        return output
