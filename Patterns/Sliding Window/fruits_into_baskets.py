def fruits_into_baskets(arr):
    basket = {}
    max_len = 0
    window_start = 0

    for window_end in range(len(arr)):
        fruit = arr[window_end]
        if fruit not in basket:
            basket[fruit] = 0
        basket[fruit] += 1

        while len(basket) > 2:
            fruit1 = arr[window_start]
            basket[fruit1] -= 1
            if basket[fruit1] == 0:
                del basket[fruit1]
            window_start += 1
        max_len = max(max_len, window_end - window_start + 1)

    return max_len


def main():
    print(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C']))


main()
