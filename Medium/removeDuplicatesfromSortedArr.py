class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0

        if len(nums) == 1:
            return 1

        n = len(nums)
        n_rep = 0
        for i in xrange(1, n):
            if nums[i] == nums[i - 1]:
                n_rep += 1
            else:
                nums[i - n_rep] = nums[i]

        return (n - n_rep)


if __name__ == '__main__':
    sol = Solution()
    nums = [1,1,1,2]
    res = sol.removeDuplicates(nums)
    print res
