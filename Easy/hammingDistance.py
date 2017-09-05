class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        z = x ^ y
        distance = 0
        while z:
            distance += 1
            z &= z - 1
        return distance

if __name__ == '__main__':
    print Solution().hammingDistance(1, 4)