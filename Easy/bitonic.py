def bitonic_search(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        middle = start + (end - start) // 2

        if arr[middle] > arr[middle + 1]:
            end = middle
        else:
            start = middle + 1

    print(arr[start])


if __name__ == '__main__':
    bitonic_search([1, 3, 8, 12, 4, 2])
    bitonic_search([3, 8, 3, 1])
    bitonic_search([1, 3, 8, 12])
    bitonic_search([10, 9, 8])
