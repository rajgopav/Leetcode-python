class Solution:
    def isPalindrome(self, s):
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum():
                print "The character is " + s[i]
                i += 1
            while i < j and not s[j].isalnum():
                print "The character is " + s[j]
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i, j = i + 1, j - 1
        return True

    def palindromeNumber(self, x):
        print str(x) == str(x)[::-1]

if __name__ == '__main__':
    #print Solution().isPalindrome("A man, a plan, a canal: Panama")
    Solution().palindromeNumber(121)

