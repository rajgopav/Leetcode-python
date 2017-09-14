class Solution:
    def targetSum(self, nums, S):
        if sum(nums) < S or (sum(nums) + S) % 2:
            return 0
        target = (sum(nums) + S) / 2
        dp = [1] + [0] * target
        for num in nums:
            for i in xrange(target, num-1, -1):
                dp[i] += dp[i-num]
        return dp[-1]

if __name__ == '__main__':
    print Solution().targetSum([1, 1, 1, 1, 1], 3)