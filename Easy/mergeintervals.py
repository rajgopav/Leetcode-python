def mergeintervals(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    iterator = iter(intervals)
    result = [next(iterator)]

    for current in iterator:
        prev = result[-1]

        if current[0] <= prev[1]:
            prev[1] = max(current[1], prev[1])
        else:
            result.append(current)
    return result


if __name__ == '__main__':
    mergeintervals([[1, 3], [2, 6], [8, 10], [15, 18]])
