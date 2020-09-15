def max_sum_contigous_subarray(arr, k):
    if not arr or not k:
        return -1

    max_sum, window_sum, window_start = 0, 0, 0
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        if window_end >= k - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[window_start]
            window_start += 1
    return max_sum


def main():
    print(max_sum_contigous_subarray([2, 1, 5, 1, 3, 2], 3))
    print(max_sum_contigous_subarray([2, 3, 4, 1, 5], 2))


main()
