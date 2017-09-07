class Solution:
    def addBinary(self, a, b):
        result, carry, value = "", 0, 0
        for i in xrange(max(len(a), len(b))):
            value = carry

            if i < len(a):
                value += int(a[- (i + 1)])
            if i < len(b):
                value += int(b[- (i + 1)])
            carry, value = value / 2, value % 2
            result += str(value)

        if carry:
            result += str(carry)
        return result[::-1]

if __name__ == '__main__':
    print Solution().addBinary("11", "1")