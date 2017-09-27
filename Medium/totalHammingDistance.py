class Solution:
    def totalHammingDistance(self, nums):
        result = 0
        for i in xrange(32):
            count = [0] * 2
            for num in nums:
                count[(num >> i) & 1] += 1
            result += count[0] * count[1]
        return result

if __name__ == '__main__':
    print Solution().totalHammingDistance([4, 14, 2])