def buyingandsellingstocks(prices):
    maxProfit = 0
    minPrice = float("INF")

    for price in prices:
        minPrice = min(minPrice, price)
        price = price - minPrice
        maxProfit = max(price, maxProfit)

    print(maxProfit)


if __name__ == "__main__":
    buyingandsellingstocks([7, 1, 5, 3, 6, 4])
