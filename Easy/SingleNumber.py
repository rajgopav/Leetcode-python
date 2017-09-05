import operator

class Solution:
    """
    :type nums: List[int]
    :rtype: int
    """
    def singleNumber(self, A):
        return reduce(operator.xor, A)

if __name__ == '__main__':
    print Solution().singleNumber([1, 1, 2, 2, 3])