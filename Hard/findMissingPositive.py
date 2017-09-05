class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        nums = list(filter(lambda x: x > 0, A))
        nums.sort()
        sample = []
        if len(nums) == 0:
            return 1
        for i in range(1, len(nums) + 2):
            sample.append(i)
        return [missing for missing in sample if missing not in nums][0]


if __name__ == "__main__":
    print Solution().firstMissingPositive([103,105,102])
    print Solution().firstMissingPositive([3, 4, -1, 1])