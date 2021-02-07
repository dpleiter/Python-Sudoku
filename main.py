import numpy

game_to_solve = 'easy-std-44-01'

class SudokuGrid:
    def __init__(self, size) -> None:
        self.size = size
        self.grid = numpy.zeros(shape=(size, size))
    
    def validate(self) -> bool:
        print(self.grid)

        checker = set()

        # Check rows
        for a in range(self.size):
            for b in range(self.size):
                val = self.grid[a, b]

                if  val != 0:
                    if val in checker:
                        raise IOError("Duplicate values")
                    else:
                        checker.add(val)

            checker.clear()

        # Check columns




        # Check boxes





        return True

with open('games/' + game_to_solve + '.in') as game:
    line = game.readline() # Grid size

    grid = SudokuGrid(int(line))

    line = game.readline() # digits

    for line in game:
        cell_info = line.split()
        coords = cell_info[0].split(',')

        grid.grid[int(coords[0]), int(coords[1])] = int(cell_info[1])

grid.validate()