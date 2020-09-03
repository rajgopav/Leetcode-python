def missingNumbers(nums):
    if not nums:
        return []

    dp = [1] * len(nums)
    for num in nums:
        dp[num - 1] = None

    return [x + 1 for x in range(len(nums)) if dp[x]]


if __name__ == '__main__':
    print(missingNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
