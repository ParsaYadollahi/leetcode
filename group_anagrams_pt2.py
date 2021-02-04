'''
  https://leetcode.com/problems/group-anagrams/
'''


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_dict = {}

        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in sorted_dict:
                sorted_dict.setdefault(sorted_word, [word])
            else:
                sorted_dict[sorted_word].append(word)

        return sorted_dict.values()
