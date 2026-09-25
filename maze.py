class Maze:
    """Find a path through a grid maze.
 
    State: (row, col) of the current square.
    Moves: up, down, left, right into any non-wall square, cost 1.
    Heuristic: Manhattan distance to the nearest goal.
    """
 
    def __init__(self, grid):
        """grid is a list of strings: '#' = wall, 'S' = start, 'G' = goal."""
        self.grid = grid
        self.goal = set()
        for r, row in enumerate(grid):
            for c, ch in enumerate(row):
                if ch == "S": # start is in the grid
                    self.start = (r, c)
                elif ch == "G": # goal is in the grid 
                    self.goal.add((r, c))
 
    def neighbors(self, state):
        r, c = state
        result = []
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(self.grid) and 0 <= nc < len(self.grid[nr]):
                if self.grid[nr][nc] != "#":
                    result.append(((nr, nc), 1))
        return sorted(result)
 
    def h(self, state):
        r, c = state
        return min(abs(r - gr) + abs(c - gc) for gr, gc in self.goal)
 
    def show(self, path):
        """Print the maze with the path drawn in dots."""
        on_path = set(path)
        for r, row in enumerate(self.grid):
            print("".join("." if (r, c) in on_path and ch == " " else ch
                          for c, ch in enumerate(row)))
 

 
# -------- DEMO of Problem ---------------

if __name__ == "__main__":
    
    from search import BFS, DFS, UCS, GreedyBestFirst, AStar # imports only called when this is the driver file 

 
    # ---- Maze ----
    grid = [
        "##########",
        "#S   #   #",
        "# ## # # #",
        "#  #   # #",
        "## ##### #",
        "#       G#",
        "##########",
    ]

    # implement the code 