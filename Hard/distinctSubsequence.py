class Solution:
    def distinctSub(self, S, T):

        ways = [0 for _ in xrange(len(T) + 1)]
        ways[0] = 1

        for s_char in S:
            for j, t_char in reversed(list(enumerate(T))):
                if s_char == t_char:
                    ways[j + 1] += ways[j]
        return ways[len(T)]

if __name__ == '__main__':
    print Solution().distinctSub("rabbbit", "rabbit")