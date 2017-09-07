class Solution:
    def pow(self, x, n):
        res = 1
        abs_n = abs(n)
        while abs_n:
            if abs_n & 1:
                res *= x
            abs_n >>= 1
            x *= x

        return 1 / res if res < 0 else res

if __name__ == '__main__':
    print Solution().pow(3,4)