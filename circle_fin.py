import re
import doctest
from itertools import combinations_with_replacement


def is_valid_email(list_email):
    flag = False
    reg = re.compile(r"(^[a-z]{1,6}_?([0-9]{0,4})?@circlefintech.com$)")
    for i in list_email:
        valid = reg.match(i)
        if valid is not None:
            print(not flag)
        else:
            print(flag)


if __name__ == "__main__":
    list_email = ["jujlia@circlefintech.com", "julia_@circlefintech.com", "julia_0@circlefintech.com",
                  "julia0_@circlefintech.com", "julia@gmail.com"]
    is_valid_email(list_email)


# On a farm divided into a grid of cells, every cell either has grass on it or is empty.

# If two adjacent cells have grass, they will belong to a common field. The common field

# extends in all directions to all adjacent cells with grass. So, if cell A is adjacent to cell

# B and cell B is adjacent to cell C, and all three have grass, then they all lie in the same

# field. If a cell with grass has no adjacent cell with grass, then it will be a field 1-cell field.

# Every field must feed one sheep or one cow. Each field of grass cannot be shared

# between cows and sheep. If each field can have one sheep or one cow and never

# both, how many possible unique arrangements can you make such that, there are

# even number of sheep in the grid farm?

# Input:

# The first line contains R (number of rows) and C (number of columns), separated by

# a space.

# Each of the next R lines contains a string with length equal to C, with no spaces. The

# string has the character Y to denote a cell with grass and N to denote a cell with no

# grass.

# Output:

# S, an integer that contains the number of arrangements possible,

# modulo 1,000,000,007.

# Constraint:

# 1 ≤ R, C ≤ 5000

# Sample Input:

# 3 4

# YNNY

# NYNY

# NYNN

# Sample Output:

# 4

# Explanation:

# There are three fields, as follows:

# 1. First Solution (zero sheep)

# 1. Cow

# 2. Cow

# 3. Cow

# 2. Second Solution (two sheep)

# 1. Sheep

# 2. Cow

# 3. Sheep

# 3. Third Solution (two sheep)

# 1. Sheep

# 2. Sheep

# 3. Cow

# 4. Fourth Solution (two sheep)

# 1. Cow

# 2. Sheep

# 3. Sheep


def mark_empty(grid, x, y):
    try:
        if not grid[x][y]:
            return
    except LookupError:
        return False
    if x < 0 or y < 0:
        return
    grid[x][y] = False
    mark_empty(grid, x + 1, y)
    mark_empty(grid, x - 1, y)
    mark_empty(grid, x, y + 1)
    mark_empty(grid, x, y - 1)

    return True


def get_spots(grid):
    """
    >>> get_spots([[True, False, True]])
    2
    >>> get_spots([[True]])
    1
    >>> get_spots([[True, False, True], [True, False, False]])
    2
    """

    spots = 0

    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if not cell:
                continue
            spots += 1
            mark_empty(grid, r, c)

    return spots


def group(grid):
    grid = [[True if c == 'Y' else False for c in row] for row in grid]

    avail_spots = get_spots(grid)

    def is_even_sheeps(combination):
        return len([_ for _ in combination if _ == 'S']) % 2 == 0

    all_comb = list(combinations_with_replacement('CS', avail_spots)) + list(
        combinations_with_replacement('SC', avail_spots))
    comb_with_even_sheeps = [c for c in all_comb if is_even_sheeps(c)]
    return len(comb_with_even_sheeps)


doctest.testmod()
assert group(['YNNY', 'NYNY', 'NYNN']) == 4
