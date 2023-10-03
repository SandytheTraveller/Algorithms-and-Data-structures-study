def minChangeRecursive(availableCoins, change):
    minCoins = change
    if change in availableCoins:
        return 1
    else:
        for i in [c for c in availableCoins if c <= change]:
            numCoins = 1 + minChangeRecursive(availableCoins, change - i)
            if numCoins < minCoins:
                minCoins = numCoins

    return minCoins

def minChangeDP(coinValueList, change):
    minCoins = [0]*(change + 1)
    coinsUsed = [0]*(change + 1)

    for cents in range(change + 1):
        coinCount = cents
        newCoin = 1

        for j in [c for c in coinValueList if c <= cents]:
            # store and re-use sub-problems results
            if minCoins[cents - j] + 1 < coinCount:
                coinCount = minCoins[cents - j] + 1
                newCoin = j