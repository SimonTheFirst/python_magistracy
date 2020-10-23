def staircase(steps: int):
    s = ""
    for step in range(1, abs(steps)+1):
        if steps > 0:
            s += ("_" * (steps - step) + "#" * step + "\n")
        else:
            s += ("_" * (step - 1) + "#" * (abs(steps) - step + 1) + "\n")
    return s


if __name__ == "__main__":
    print(staircase(3))
    print(staircase(-8))
