#!/usr/bin/python3

# Exercise 1 : Conway’s Game of Life
# What you will create

# Instructions
#
# These are the rules of the Game of Life (as stated in Wikipedia):
#
# The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, each of which is in one 
# of two possible states, alive or dead, (or populated and unpopulated, respectively). 


#    Any live cell with fewer than two live neighbours dies, as if by underpopulation.
#    Any live cell with two or three live neighbours lives on to the next generation.
#    Any live cell with more than three live neighbours dies, as if by overpopulation.
#    Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

#Using these rules, implement the Game. (Hint: use Classes !!!!)
#Use a few different initial states to see how the game ends.
#
#Notes:
#
#    Display the grid after each generation
#    The end of the game is fully determined by the initial state. So have it pass through your program and see how it ends.
#    Be creative, but use classes
#    The game can have fixed borders and can also have moving borders. First implement the fixed borders. Each “live” cell that is going out of the border, exits the game.
#   Bonus: Make the game with ever expandable borders, make the maximum border size a very large number(10,000) so you won’t cause a memory overflow

#TODO: Bonus


class Board:
    def __init__(self, board_x_size, board_y_size):
        self.grid = []
        
        for y in range(board_y_size):
            row = []
            for x in range(board_x_size):
                row.append(Cell("-", x, y))
            self.grid.append(row)
        #return self.grid
    
    def show_board(self):
        for row in self.grid:
            print(" ".join(["a" if cell.state == "alive" else "-" for cell in row]))
    
    def run_generation(self):
        new_grid = []

        for y in range(len(self.grid)):
            new_row = []
            for x in range(len(self.grid[0])):
                cell = self.grid[y][x]
                new_state = cell.define_state(self.grid)
                new_row.append(Cell(new_state, x, y))
            new_grid.append(new_row)

        self.grid = new_grid



class Cell:
    def __init__(self, state, x, y):
        self.state = state
        self.x = x
        self.y = y
    
    def count_neighbours(self, grid):
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            ( 0, -1),          ( 0, 1),
            ( 1, -1), ( 1, 0), ( 1, 1)
        ]

        count = 0
        max_y = len(grid)
        max_x = len(grid[0]) if max_y > 0 else 0

        for dx, dy in directions:
            nx, ny = self.x + dx, self.y + dy

            if 0 <= nx < max_x and 0 <= ny < max_y:
                neighbor = grid[ny][nx]
                if neighbor.state == "alive":
                    count += 1

        return count

    def define_state(self, cell):

        #Any live cell with fewer than two live neighbours dies, as if by underpopulation.
        #Any live cell with two or three live neighbours lives on to the next generation.
        #Any live cell with more than three live neighbours dies, as if by overpopulation.
        #Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

        alive_neighbors = self.count_neighbours(cell)

        if self.state == "alive":
            if alive_neighbors < 2 or alive_neighbors > 3:
                return "dead"
            else:
                return "alive"
        else:  #dead
            if alive_neighbors == 3:
                return "alive"
            else:
                return "dead"

def run_states(self,grade):
    new_grid = []

    for y in range(len(self.grid)):
        new_row = []
        for x in range(len(self.grid[0])):
            cell = self.grid[y][x]
            new_state = cell.define_state(self.grid)
            new_row.append(Cell(new_state, x, y))
        new_grid.append(new_row)

    self.grid = new_grid


board = Board(20, 20)

board.grid[1][1].state = "alive"
board.grid[1][2].state = "alive"
board.grid[1][3].state = "alive"
board.grid[3][1].state = "alive"
board.grid[5][2].state = "alive"
board.grid[6][3].state = "alive"
board.grid[3][1].state = "alive"
board.grid[5][2].state = "alive"
board.grid[6][3].state = "alive"

board.show_board()
print("Generation 1:")
board.show_board()

board.run_generation()
print("\nGeneration 2:")
board.show_board()

board.run_generation()
print("\nGeneration 3:")
board.show_board()