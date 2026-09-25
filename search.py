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


# --------------------------- BFS -------------------------------

class BFS:
    """Class for BFS Search"""

    def __init__(self, problem):
        self.problem = problem # the problem is an object 
        self.explored = set()
        self.frontier = f.Queue()


    def update(self, state, g=0, path=None):
        """Adding a state to the frontier"""
        if path is None: 
            path = [state]
        priority = 0 # no priority
        self.frontier.add((priority, g, state, path)) # no priority

    def search(self):
        """ BFS Search function """

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

# --------------------------- DFS -------------------------------

class DFS:
    """Class for DFS Search"""

    def __init__(self, problem):
        self.problem # the problem is an object 
        self.explored = set()
        self.frontier = f.Stack()


    def update(self, state, g=0, path=None):
        """Adding a state to the frontier"""
        if path is None: 
            path = [state]
        priority = 0 # no priority
        self.frontier.add((priority, g, state, path)) # no priority

    def search(self):
        """ DFS Search function """

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

# --------------------------- UCS ----------------------------
class UCS:
    """Class for Uniform Cost Search"""

    def __init__(self, problem):
        self.problem # the problem is an object 
        self.explored = set()
        self.frontier = f.PriorityQueue()


    def update(self, state, g=0, path=None):
        """Adding a state to the frontier"""
        if path is None: 
            path = [state]
        priority = g
        self.frontier.add((priority, g, state, path))

    def search(self):
        """ UCS Search function """

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
        
        return None                    # no path found!

# --------------------------- Greedy Best-First ----------------------------
class GreedyBestFirst:
    """Class for Greedy Best First"""

    def __init__(self, problem):
        self.problem # the problem is an object 
        self.explored = set()
        self.frontier = f.PriorityQueue()


    def update(self, state, g=0, path=None):
        """Adding a state to the frontier"""
        if path is None: 
            path = [state]
        priority = self.problem.h(state) 
        self.frontier.add((priority, g, state, path)) #priority only determined by h! 

    def search(self):
        """ UCS Search function """

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
        
        return None                    # no path found!

# --------------------------- A* -------------------------------

class AStar:
    """Class for A* Search"""

    def __init__(self, problem):
        self.problem # the problem is an object 
        self.explored = set()
        self.frontier = f.PriorityQueue()


    def update(self, state, g=0, path=None):
        """Adding a state to the frontier"""
        if path is None: 
            path = [state]
        priority = g + self.problem.h(state) # problem must contain a heuristic method called h()
        self.frontier.add((priority, g, state, path))

    def search(self):
        """ A* Search function """

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

  
