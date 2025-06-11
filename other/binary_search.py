def binary_search(values, cost):
    # print("values: {0}, cost: {1}".format(values, cost))
    begin = 0
    end = len(values) - 1

    while begin <= end:
        mid = (begin + end) // 2
        value = values[mid]
        # print("begin: {0}, end: {1}, mid: {2}, value: {3}".format(begin, end, mid, value))

        if value == cost:
            # print("Found!")
            return mid

        if value < cost:
            # print("Moving begin!")
            begin = mid + 1
            continue

        if value > cost:
            # print("Moving end!")
            end = mid - 1
            continue
    
    # print("Not found!")
    return None