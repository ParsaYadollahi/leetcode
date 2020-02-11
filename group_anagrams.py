'''
    https://leetcode.com/explore/interview/card/microsoft/30/array-and-strings/200/
'''


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a dictionary for each associated word

        sorted_strs = []
        for word in strs:
            sorted_strs.append(''.join(sorted(word)))

        # remove duplicates by creating set then back to list
        sorted_strs = list(set(sorted_strs))
        sorted_dict = {sorted_strs[i]: [] for i in range(len(sorted_strs))}
        for word in strs:
            sorted_dict[''.join(sorted(word))].append(word)

        return sorted_dict.values()
