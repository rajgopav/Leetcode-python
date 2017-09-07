import collections

class Solution:
    def groupAnagrams(self, strs):
        anagrams_map, result =  collections.defaultdict(list), []
        for s in strs:
            sorted_str = "".join(sorted(s))
            anagrams_map[sorted_str].append(s)
        for anagram in anagrams_map.values():
            anagram.sort()
            result.append(anagram)
        return result

if __name__ == '__main__':
    print Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])

