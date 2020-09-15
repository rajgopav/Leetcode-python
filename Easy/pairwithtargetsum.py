def targetSum(arr, target):
    if not arr or not target:
        return []

    i = 0
    j = len(arr) - 1
    sum = 0

    while i < j:
        if arr[i] + arr[j] == target:
            return [i, j]
        elif arr[i] + arr[j] < target:
            i += 1
        elif arr[i] + arr[j] > target:
            j -= 1

    print("No element in arr")


if __name__ == "__main__":
    print(targetSum([2, 5, 9, 11], 11))
