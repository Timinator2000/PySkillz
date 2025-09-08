```python
class Cell():

    xy = False

    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value
        self.neighbors = dict()


    def add_neighbor(self, direction, cell):
        self.neighbors[direction] = cell


    def loc(self):
        return (self.row, self.col) if not Cell.xy else (self.col, self.row)


    def is_open(self):
        return True


    def get_neighbor(self, direction):
        return None if direction not in self.neighbors else self.neighbors[direction]


    def get_all_neighbors(self):
        return list(self.neighbors.values())


    def __lt__(self, other):
        return self.loc() < other .loc()


    def __str__(self):
        return f'{self.loc()}'
        

class Grid():

    def __init__(self, grid: list[list], diags=False, wrap_up_down=False, wrap_left_right=False):
        self.height = len(grid)
        self.width = len(grid[0])

        self.grid = {(r, c): self.create_cell(r, c, value) for r, row in enumerate(grid) for c, value in enumerate(row)}

        deltas = [('N', (-1, 0)), ('S', (1, 0)), ('E', (0, 1)), ('W', (0, -1))]
        if diags:
            deltas += [('NE', (-1, 1)), ('NW', (-1, -1)), ('SE', (1, 1)), ('SW', (1, -1))]
        
        for r in range(self.height):
            for c in range(self.width):
                cell = self.grid[(r,  c)]
                for direction, (dr, dc) in deltas:
                    nr = r + dr
                    nc = c + dc

                    if wrap_up_down:
                        nr = (nr + self.height) % self.height

                    if wrap_left_right:
                        nc = (nc + self.width) % self.width

                    if (nr, nc) not in self.grid:
                        continue

                    neighbor = self.grid[(nr, nc)]
                    if cell.is_open() and neighbor.is_open():
                        cell.add_neighbor(direction, neighbor)


    def create_cell(self, r, c, value):
        return Cell(r, c, value)


    def all_cells(self):
        return self.grid.values()


    def find_cells(self, value):
        return [cell for cell in self.grid.values() if cell.value == value]


    def __str__(self):
        grid = [[self.grid[(r, c)].value for c in range(self.width)] for r in range(self.height)]
        return '\n'.join(''.join(row) for row in grid)



# from Grid import Grid, Cell


class PeaksAndValleysCell(Cell):

    def __lt__(self, other):
        return self.loc()[::-1] < other.loc()[::-1]


class PeaksAndValleysGrid(Grid):

    def create_cell(self, r, c, value):
        return PeaksAndValleysCell(r, c, value)


Cell.xy = True
grid = PeaksAndValleysGrid([[int(i) for i in input().split()] for _ in range(int(input()))], diags=True)

peaks = [c for c in grid.all_cells() if all(c.value > n.value for n in c.get_all_neighbors())]
valleys = [c for c in grid.all_cells() if all(c.value < n.value for n in c.get_all_neighbors())]

print('NONE' if not peaks else ', '.join(f'{c}' for c in sorted(peaks)))
print('NONE' if not valleys else ', '.join(f'{c}' for c in sorted(valleys)))
```