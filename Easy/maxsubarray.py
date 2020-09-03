def maxsubarray(nums):
    if not nums:
        return 0

    if max(nums) < 0:
        return max(nums)

    minsum = maxsum = 0

    for elem in nums:
        minsum = max(0, minsum + elem)
        maxsum = max(minsum, maxsum)

    print(maxsum)


if __name__ == '__main__':
    maxsubarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
