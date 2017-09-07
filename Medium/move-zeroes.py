class Solution(object):
    def move_zeroes(self, nums):
        pos = 0
        for x in xrange(len(nums)):
            if nums[x]:
                nums[pos] = nums[x]
                pos += 1

        for i in xrange(pos, len(nums)):
            nums[i] = 0

        print nums

    def move_zeroes2(self, nums):
        pos = 0
        for i in xrange(len(nums)):
            if nums[i]:
                nums[i], nums[pos] = nums[pos], nums[i]
                pos += 1

def main():
    s = Solution()
    #s.move_zeroes([0, 1, 0, 3, 12])
    s.move_zeroes2([0, 1, 0, 3, 12])

if __name__ == '__main__':
    main()