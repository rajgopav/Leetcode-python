class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = [None]*len(nums)
        left[0] = 1
        for i in xrange(1, len(nums)):
            left[i] = left[i - 1] * nums[i - 1]
        right = 1
        for i in xrange(len(nums) - 2, -1, -1):
            right *= nums[i + 1]
            left[i] *= right
        return left

if __name__ == '__main__':
    print Solution().productExceptSelf([1,2,3,4])