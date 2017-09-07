class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        distance = 0
        z = x ^ y
        while z:
            distance += 1
            z &= z - 1
        return distance

def main():
    solution = Solution()
    res = solution.hammingDistance(1,4)
    print res

if __name__ == '__main__':
    main()