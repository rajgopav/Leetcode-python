import collections


class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = 1
        n = nums[0]
        for i in nums[1:]:
            if i == n:
                c += 1
            else:
                c -= 1
                if c == 0:
                    c = 1
                    n = i
        return n


if __name__ == "__main__":
    print Solution().majorityElement([1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 6])