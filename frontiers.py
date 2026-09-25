
class Frontier:
    """ Parent class for Queues, Stacks, and Priority Queues"""

    def __init__(self):
        """Constructor"""
        self.frontier = []

    def pop(self):
        """Remove from frontier"""
        return self.frontier.pop(0) # removes from the beginning 
    
    def is_empty(self):
        return len(self.frontier) == 0

class Stack(Frontier):
    """
    A class to define a stack 
    """

    def add(self, state):
        """Add to the stack"""
        self.frontier.insert(0, state) # add at the beginning 

class Queue(Frontier):
    """
    A class to define a queue 
    """

    def add(self, state):
        """Add to the queue"""
        self.frontier.append(state) # add at the end 

class PriorityQueue(Frontier): 
    """
    A class to define a priority queue

    For this, we need to enforce tuples  
    """

    def add(self, state):
        """Add to the priority queue"""
        if type(state) != tuple:
            raise TypeError("Priority Queue requires Tuple entries")
        if type(state[0]) != int and type(state[0]) != float:
            raise TypeError("First entry of tuple must be numeric")
        self.frontier.append(state) # add at the end
        self.frontier.sort()

# challenge: 
# build a parent class for the 5 algorithms we've covered: 
# BFS, DFS, UCS, Greedy Best-first, A*

if __name__ == "__main__":
    print("hello")
    # my_stack = Stack() # creating stack 
    # print("Stack Made")

    # my_stack.add("hello")
    # print("Hello added to stack")

    # my_stack.add("How")
    # my_stack.add("are")
    # my_stack.add("you")
    # print("'How, are, you' added to stack")

    # while not my_stack.is_empty(): # remove items from stack
    #     print(my_stack.pop())
    # print("Stack is empty")

    # my_queue = Queue() # creating stack 
    # print("Queue Made")

    # my_queue.add("hello")
    # print("Hello added to queue")

    # my_queue.add("How")
    # my_queue.add("are")
    # my_queue.add("you")
    # print("'How, are, you' added to stack")

    # while not my_queue.is_empty(): # remove items from stack
    #     print(my_queue.pop())
    # print("Queue is empty")