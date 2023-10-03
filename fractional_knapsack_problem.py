def fractionalKnapsack(W, items):
    # sorting item on basis of value/weight ratio
    # sorting using a lambda function - short anonymous function
    # that execute one expression
    items.sort(key=lambda x: (x.value / x.weight), reverse=True)

    maxValue = 0.0
    chosen_items = []
    capacity = W

    for item in items:
        # if the weight of the item does not exceed the knapsack
        # capacity, add it completely and reduce the remaining capacity
        if item.weight <= W:
            capacity -= item.weight
            maxValue += item.value
            chosen_items.append(item)

        else:
            # if the weight of the item will exceed the
            # knapsack capacity, add a fraction of it to fill in
            # the knapsack and end the cycle
            fractional_value = item.value * W / item.weight
            maxValue += fractional_value

            chosen_items.append(item)
            break

    return maxValue, chosen_items
