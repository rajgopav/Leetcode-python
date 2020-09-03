def lcs(nums):
    numset = set(nums)
    res = 0

    for elem in nums:
        if elem - 1 not in numset:
            y = elem + 1
            while y in numset:
                y += 1
            res = max(res, y - elem)
    print(res)


if __name__ == '__main__':
    lcs([100, 4, 200, 1, 3, 2])
