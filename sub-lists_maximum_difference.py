def subListsMaxDiff(num_list, N, k):
    # sort the array in descending order
    num_list.sort(reverse=True)

    # find the largest number
    M = max(k, N - k)

    S1 = num_list[0:M] # the largest sub-list will contain the largest numbers
    S2 = num_list[M:]

    max_difference = sum(S1) - sum(S2)

    return S1, S2, max_difference


if __name__ == "__main__":
    num_list = [7, 10, 2, 15, 30, 5, 22]
    N = len(num_list)
    k = 3
    print(subListsMaxDiff(num_list, N, k))