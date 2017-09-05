class Solution():
    def sqrt(self, x):
        if x < 2:
            return x

        if x == 0: return 0
        l, r = 1, x
        while r - l > 1:
            mid = (l + r) // 2
            if mid * mid > x:
                r = mid
            else:
                l = mid
        return l

if __name__ == '__main__':
    print Solution().sqrt(10)