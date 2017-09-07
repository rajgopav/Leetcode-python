class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):

        num_set = set(num)
        max_length = 0

        for elem in num_set:
            count = 0
            left = elem - 1
            right = elem + 1

            while left in num_set:
                count += 1
                num_set.remove(left)
                left -= 1

            while right in num_set:
                count += 1
                num_set.remove(right)
                right += 1

            max_length = max(max_length, count)

        return max_length

if __name__ == "__main__":
    print Solution().longestConsecutive([100, 4, 200, 1, 3, 2])