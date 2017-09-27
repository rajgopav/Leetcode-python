class Solution:
    def maxSwap(self, nums):
        digits = list(str(nums))
        left, right = 0, 0
        max_indx = len(digits) - 1
        for i in reversed(xrange(len(digits))):
            if digits[i] > digits[max_indx]:
                max_indx = i
            elif digits[max_indx] > digits[i]:
                left, right = i, max_indx
        digits[left], digits[right] = digits[right], digits[left]
        return int("".join(digits))

if __name__ == '__main__':
    print Solution().maxSwap(2736)
