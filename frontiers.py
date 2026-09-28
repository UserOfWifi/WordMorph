class Frontier:
    """Parent class for Queues, Stacks, and Priority Queues."""

    def __init__(self):
        """Constructor"""
        self.frontier = []

    def pop(self):
        """Remove and return the first item from the frontier."""
        return self.frontier.pop(0)

    def is_empty(self):
        """Return True if the frontier is empty."""
        return len(self.frontier) == 0


class Stack(Frontier):
    """A class to define a stack."""

    def add(self, state):
        """Add an item to the stack."""
        # Stack = Last In, First Out
        self.frontier.insert(0, state)


class Queue(Frontier):
    """A class to define a queue."""

    def add(self, state):
        """Add an item to the queue."""
        # Queue = First In, First Out
        self.frontier.append(state)


class PriorityQueue(Frontier):
    """A class to define a priority queue."""

    def add(self, state):
        """Add an item to the priority queue."""

        # UCS, Greedy, and A* will use tuples such as:
        # (priority, word)

        if type(state) != tuple:
            raise TypeError("Priority Queue requires Tuple entries")

        if type(state[0]) != int and type(state[0]) != float:
            raise TypeError("First entry of tuple must be numeric")

        self.frontier.append(state)

        # Keep the smallest priority at the front.
        self.frontier.sort()