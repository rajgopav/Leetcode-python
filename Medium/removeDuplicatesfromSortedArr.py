class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        last, curr = 0, 1
        while curr < len(nums):
            if nums[last] != nums[curr]:
                last += 1
                nums[last] = nums[curr]
            curr += 1
        return last + 1

if __name__ == '__main__':
    sol = Solution()
    nums = [1,1,1,2]
    res = sol.removeDuplicates(nums)
    print res
