import frontiers as f

""" This module requires a *problem* object implementing the following interface:

Attributes
----------
start : state
    The initial state of the search.
goal : set of states
    The collection of goal states, stored as a SET so that
    membership tests (``state in problem.goal``) are O(1).

Methods
-------
neighbors(state) -> iterable of (state, cost) pairs

h(state) -> returns the heuristic value 
"""




class Search: 
    """Parent class for the 5 search methods from CSCI 325.
    """


    def __init__(self, problem, frontier):
        self.problem = problem
        self.explored = set()
        self.frontier = frontier # set in child classes 
    
    def priority(self, state, g):
        """Child classes must override"""
        raise NotImplementedError("Subclasses must define priority")

    def update(self, state, g=0, path=None):
        """Adding a state to the frontier"""
        if path is None: 
            path = [state]
        self.frontier.add((self.priority(state, g), g, state, path)) 
    
    def search(self):
        """Generic search function that works for all 5 algorithms!"""

        self.update(self.problem.start)

        while not self.frontier.is_empty():
            _, g, state, path = self.frontier.pop()
            
            if state in self.problem.goal:  
                return path, g   
            
            if state in self.explored:  
                continue          
            
            self.explored.add(state)
            for nbr, w in self.problem.neighbors(state):         
                if nbr not in self.explored:
                    self.update(nbr, g + w, path + [nbr])
        
        return None    


# --------------------------- BFS -------------------------------

class BFS(Search):
    """Class for BFS Search"""

    def __init__(self, problem):
        super().__init__(problem, f.Queue()) # calls the constructor from the parent class
    
    def priority(self, state, g):
        return 0 # no priority used
    
 

# --------------------------- DFS -------------------------------

class DFS(Search):
    """Class for DFS Search"""

    def __init__(self, problem):
        super().__init__(problem, f.Stack()) # calls the constructor from the parent class

    def priority(self, state, g):
        return 0 # no priority used

# --------------------------- UCS ----------------------------
class UCS(Search):
    """Class for Uniform Cost Search"""

    def __init__(self, problem):
        super().__init__(problem, f.PriorityQueue()) # calls the constructor from the parent class


    def priority(self, state, g):
        return g 

# --------------------------- Greedy Best-First ----------------------------
class GreedyBestFirst(Search):
    """Class for Greedy Best First"""

    def __init__(self, problem):
        super().__init__(problem, f.PriorityQueue()) # calls the constructor from the parent class


    def priority(self, state, g):
        return self.problem.h(state)

# --------------------------- A* -------------------------------

class AStar(Search):
    """Class for A* Search"""

    def __init__(self, problem):
        super().__init__(problem, f.PriorityQueue()) # calls the constructor from the parent class

    def priority(self, state, g):
        return self.problem.h(state) + g