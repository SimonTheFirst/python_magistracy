def can_see_stage(hall):
    for col in range(len(hall[0])):
        curr_seat = hall[0][col]
        for row in range(1, len(hall)):
            if curr_seat >= hall[row][col]:
                return False
            else:
                curr_seat = hall[row][col]
    return True


if __name__ == "__main__":
    test1 = [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
            ]
    print(can_see_stage(test1))

    test2 = [[1, 2, 3, 2, 1, 1],
            [2, 4, 4, 3, 2, 2],
            [5, 5, 5, 10, 4, 4],
            [6, 6, 7, 6, 5, 5]]
    print(can_see_stage(test2))

