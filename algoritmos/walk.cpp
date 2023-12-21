#include <iostream>
#include <vector>

bool is_valid_walk(const std::vector<char> &walk) {
    int north = 0, south = 0, west = 0, east = 0;

    for (char direction : walk) {
        if (direction == 'n') {
            north += 1;
        } else if (direction == 's') {
            south += 1;
        } else if (direction == 'w') {
            west += 1;
        } else if (direction == 'e') {
            east += 1;
        }
    }

    return (north == south && west == east);
}

int main() {
    std::vector<char> passos = {'n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's'};

    if (is_valid_walk(passos)) {
        std::cout << "True" << std::endl;
    } else {
        std::cout << "False" << std::endl;
    }

    return 0;
}
