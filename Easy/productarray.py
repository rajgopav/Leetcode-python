def productarray(nums):
    if not nums:
        return []

    left_product = [1 for _ in range(len(nums))]

    for i in range(1, len(nums)):
        left_product[i] = left_product[i - 1] * nums[i - 1]

    right_product = 1
    for i in range(len(nums) - 2, -1, -1):
        right_product *= nums[i + 1]
        left_product[i] = left_product[i] * right_product

    print(left_product)


if __name__ == "__main__":
    productarray([1, 2, 3, 4])
