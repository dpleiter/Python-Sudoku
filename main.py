import numpy
import math

game_to_solve = 'easy-std-44-01'

class SudokuGrid:
    def __init__(self, size) -> None:
        self.size = size
        self.grid = numpy.zeros(shape=(size, size))
    
    def validate(self) -> bool:
        # Check rows
        for row_num in range(self.size):
            if contains_duplicates(self.grid[row_num]):
                return False
        
        # Check columns
        for col_num in range(self.size):
            if contains_duplicates(self.grid[:,col_num]):
                return False

        # Check boxes
        for box_num in range(self.size):
            box_size = int(math.sqrt(self.size))

            rows = (box_size * int(box_num / box_size), box_size * (1 + int(box_num / box_size)))
            cols = ((box_num % box_size) * box_size, (box_num % box_size + 1) * box_size)

            box = self.grid[rows[0] : rows[1], cols[0] : cols[1]].flatten()

            if (contains_duplicates(box)):
                return False

        return True

def contains_duplicates(arr) -> bool:
    checker = set()

    for x in arr.flatten():
        if x == 0:
            continue
        
        if x in checker:
            return True
        else:
            checker.add(x)

    return False

with open('games/' + game_to_solve + '.in') as game:
    line = game.readline() # Grid size

    grid = SudokuGrid(int(line))

    line = game.readline() # digits

    for line in game:
        cell_info = line.split()
        coords = cell_info[0].split(',')

        grid.grid[int(coords[0]), int(coords[1])] = int(cell_info[1])

    print(grid.grid)

if grid.validate():
    print("All good")
else:
    print("Invalid Grid")