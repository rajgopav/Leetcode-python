def longest_substring_k_distinct(arr, K):
    res = {}
    window_start = 0
    max_len = 0

    for window_end in range(len(arr)):
        ch = arr[window_end]
        if ch not in res:
            res[ch] = 0
        res[ch] += 1

        while len(res) > K:
            ch1 = arr[window_start]
            res[ch1] -= 1
            if res[ch1] == 0:
                del res[ch1]
            window_start += 1

        max_len = max(max_len, window_end - window_start + 1)
    return max_len


def main():
    print(longest_substring_k_distinct("araaci", 2))
    print(longest_substring_k_distinct("araaci", 1))
    print(longest_substring_k_distinct("cbbebi", 3))


main()
