def DP_Knapsack(W, items):
    num_items = len(items)
    # initialize an empty table of size (W + 1) x (N + 1)
    DP_table = [[0 for x in range(W + 1)] for x in range(num_items + 1)]

    # find the max value
    for i in range(num_items + 1):
        for wt in range(W + 1):
            if i == 0 or wt == 0:
                DP_table[i][wt] = 0
            elif items[i - 1].weight <= wt:
                DP_table[i][wt] = max(items[i - 1].value +
                            DP_table[i - 1][wt - items[i - 1].weight],
                                        DP_table[i - 1][wt])
            else:
                DP_table[i][wt] = DP_table[i - 1][wt]
    maxValue = DP_table[num_items][W]

    chosen_items = []
    res = maxValue
    # find the items that get the max value
    for i in range(num_items, 0, -1):
        if res <= 0:
            break

        if res != DP_table[i - 1][W]:
            chosen_items.append(items[i - 1])
            res = res - items[i - 1].value
            W = W - items[i - 1].weight

    return maxValue, chosen_items