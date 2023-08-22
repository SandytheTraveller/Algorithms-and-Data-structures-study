def print_movement(n, source, destination):
    print("Move disk", n, "from rod", source, "to rod", destination)


def Tower_of_Hanoi(n, source, destination, auxiliary):
    if n == 1:
        print_movement(1, source, destination)
        return

    Tower_of_Hanoi(n - 1, source, auxiliary, destination)
    print_movement(n, source, destination)
    Tower_of_Hanoi(n - 1, auxiliary, destination, source)


n = 3
Tower_of_Hanoi(n, 'A', 'C', 'B')
