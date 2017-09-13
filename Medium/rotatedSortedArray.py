class Solution():
    class Solution(object):
        def search(self, nums, target):
            """
            :type nums: List[int]
            :type target: int
            :rtype: int
            """
            lo, high = 0, len(nums) - 1
            while lo < high:
                mid = (lo + high) / 2
                if (nums[0] > target) ^ (nums[0] > nums[mid]) ^ (target > nums[mid]):
                    lo = mid + 1
                else:
                    high = mid
            return lo if target in nums[lo:lo + 1] else -1

