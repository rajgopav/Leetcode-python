class Solution(object):
    def multiply(self, A, B):
        m, n, l = len(A), len(A[0]), len(B[0])
        res = [[0 for _ in xrange(l)] for _ in xrange(m)]
        for i in xrange(m):
            for k in xrange(n):
                if A[i][k]:
                    for j in xrange(l):
                        res[i][j] += A[i][k] * B[k][j]
        return res

def main():
        A = [[1, 0, 0], [-1, 0 ,3]]
        B = [[7, 0 , 0],[0 ,0, 0],[0, 0 , 1]]
        solution = Solution()
        res = solution.multiply(A, B)
        print res

if __name__ == "__main__":
    main()