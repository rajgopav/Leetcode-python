def findduplicate(nums):
    if not nums:
        return 0

    while nums[nums[0]] != nums[0]:
        nums[nums[0]], nums[0] = nums[0], nums[nums[0]]
    print(nums[0])


if __name__ == '__main__':
    findduplicate([1, 3, 4, 2, 2])
