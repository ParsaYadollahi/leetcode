'''
    https://leetcode.com/problems/check-if-n-and-its-double-exist/
'''
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        s = set(arr)
        count = 0
        for i in arr:
            if i == 0:
                count += 1
                if count == 2:
                    return True
            elif i*2 in s:
                return True
        return False


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        d = {}
        for i in arr:
            if i in d:
                d[i] += 1

            else:
                d[i] = 1
        if 0 in d and d[0] > 1:
            return True
        else:
            for k in d:
                if k == 0:
                    continue
                elif k*2 in d:
                    return True
        return False
