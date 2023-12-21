def is_valid_walk(walk):
    north = 0
    south = 0
    west = 0
    east = 0

    if len(walk) == 10:
        for times, char in enumerate(walk):
            if char == "n":
                north += 1
            if char == "s":
                south += 1
            if char == "e":
                east += 1
            if char == "w":
                west += 1

        if north == south and west == east:
            return True

        else:
            return False

    else:
        return False


def test():
    assert is_valid_walk(["n", "s", "n", "s", "n", "s", "n", "s", "n", "s"]) == True
    assert is_valid_walk(["w", "e", "w", "e", "w", "e", "w", "e", "w", "e", "w", "e"]) == False
    assert is_valid_walk(["w"]) == False
    assert is_valid_walk(["n", "n", "n", "s", "n", "s", "n", "s", "n", "s"]) == False
