class VacuumCleaner:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.current_row = 0
        self.current_col = 0

    def clean(self):
        while True:
            # Clean the current cell
            print("Moving to cell ({}, {}) and cleaning...".format(self.current_row, self.current_col))
            self.grid[self.current_row][self.current_col] = 0  # Mark cell as clean
            
            # Move to the next dirty cell
            next_row, next_col = self.find_next_dirty_cell()
            if next_row is None and next_col is None:
                print("All cells cleaned!")
                break
            else:
                self.current_row, self.current_col = next_row, next_col

    def find_next_dirty_cell(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col] == 1:  # Check if cell is dirty
                    return row, col
        return None, None

# Example usage
grid = [
    [1, 0, 0, 1],
    [0, 1, 1, 0],
    [1, 1, 0, 0]
]

vacuum = VacuumCleaner(grid)
vacuum.clean()
