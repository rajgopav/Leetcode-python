class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        currLength = maxlength = 0
        list = []
        for i in xrange(0, len(s)):
            curr_char = s[i]

            if curr_char not in list:
                list.append(curr_char)
                currLength += 1
            else:
                list = []
                currLength = 0

            if currLength > maxlength:
                maxlength = currLength
        return maxlength

    def lengthOfLongestSubstring2(self,s):
        longest, start, visit = 0, 0, [False for _ in xrange(256)]
        for i, char in enumerate(s):
            if visit[ord(char)]:
                while char != s[start]:
                    visit[ord(s[start])] = False
                    start += 1
                start += 1
            else:
                visit[ord(char)] = True
            longest = max(longest, i - start + 1)
        return longest

if __name__ == '__main__':
    print Solution().lengthOfLongestSubstring2("aab")