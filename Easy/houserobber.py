class Solution():
    def rob(self, nums):
        if not nums:
            return 0
        n = len(nums)
        dp = [0] * (n+1)
        dp[1] = nums[0]
        for i in xrange(2,n+1):
            dp[i] = max(dp[i-2] + nums[i-1], dp[i-1])
        return dp[n]

if __name__ == '__main__':
    print Solution().rob([8,4,8,5,9,6,5,4,4,10])