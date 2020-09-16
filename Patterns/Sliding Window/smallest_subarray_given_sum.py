import math


def smallest_subarray_sum(arr, K):
    if not arr or not K:
        return -1

    min_len, window_sum, window_start = math.inf, 0, 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        while window_sum >= K:
            min_len = min(window_end - window_start + 1, min_len)
            window_sum -= arr[window_start]
            window_start += 1
    if min_len == math.inf:
        return 0
    return min_len

def main():
    print(smallest_subarray_sum([3, 4, 1, 1, 6], 8))


main()
