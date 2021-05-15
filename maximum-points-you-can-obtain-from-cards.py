'''
    https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
'''
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l, r = 0, k

        leftSubArr = cardPoints[0:k]
        rightSubArr = cardPoints[len(cardPoints)-k:len(cardPoints)]
        cardPointsK = rightSubArr + leftSubArr

        max_sum = sum(cardPointsK[0:k])
        curr_sum = max_sum

        while(r < len(cardPointsK)):
            curr_sum -= cardPointsK[l]
            curr_sum += cardPointsK[r]

            max_sum = max(curr_sum, max_sum)
            l += 1
            r += 1

        return max_sum
