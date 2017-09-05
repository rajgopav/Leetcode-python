class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """

        if not triangle:
            return 0



if __name__ == "__main__":
    print Solution().minimumTotal([[-1], [2, 3], [1, -1, -3]])
