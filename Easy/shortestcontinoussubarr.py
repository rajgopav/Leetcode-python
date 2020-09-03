def shortest(nums):
    for i in range(1, len(nums)):
        if nums[i - 1] > nums[i]:
            left = i
            break

    for i in range(len(nums) - 2, 0, -1):
        if nums[i + 1] < nums[i]:
            right = i
            break
    print()


if __name__ == "__main__":
    shortest([2, 6, 4, 8, 10, 9, 15])
