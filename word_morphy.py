
import pandas as pd
import frontiers as f
import time

print("Frontiers file being used:", f.__file__)
print("Has Queue:", hasattr(f, "Queue"))

data = pd.read_excel(
    
    "Copy of SUBTLEX-US frequency list with cost.xlsx"
)

dictionary = set(data["Word"].dropna().str.upper())

cost_of = dict(zip(data["Word"].str.upper(), data["Cost"].astype(int)))
#creates a dictionary that maps each word directly to its cost, this avoids searching through the entire pandas dataframe every time the cost if a word is needed

from collections import defaultdict
#Build an index of words using patterns with one letter removed, 
#words that share the same pattern differs only by one letter, 
#building this index once prevents us from scanning the entire dictionary every time we need to find neighbors
neighbor_index = defaultdict(set)

for word in dictionary:
    for i in range(len(word)): #creates on epattern for each letter position

        #replace one letter with "-" to create a pattern
        pattern = word[:i] + "_" + word[i+1:]

        #store the word under that pattern
        neighbor_index[pattern].add(word)



def get_neighbors(word, neighbor_index):
    """
    Find all words that differ from 'word' by exactly one letter.
    """

    neighbors = set()

    for i in range(len(word)):
        pattern = word[:i] + "_" + word[i+1:]

        for candidate in neighbor_index.get(pattern, set()):

            if candidate != word:
                neighbors.add(candidate)

    return sorted(neighbors)




def get_cost(word):
    """
    #look up the word's cpst directly in the cost dictionary
    """
    return cost_of[word.upper()]

    #row = data[data["Word"].str.upper() == word.upper()].iloc[0]

    #return int(row["Cost"])


class SearchAlgorithm:
    """
    Parent class for BFS, DFS, UCS, Greedy, and A*.
    """

    def __init__(self, start, goal, dictionary, data, frontier):

        self.start = start
        self.goal = goal

        # The SUBTLEX word list acts as our dictionary.
        self.dictionary = dictionary

        # The dataset contains the cost of each word.
        self.data = data

        # Queue, Stack, or PriorityQueue.
        self.frontier = frontier

        # Keep track of words already explored.
        self.explored = set()

        # Keep track of the current word.
        self.current_state = None

        # Keep track of the path to each word.
        self.paths = {
            start: [start]
        }

    def search(self):
        """
        Search from the start word until the goal is found.
        """

        # Add the starting word to the frontier.
        self.add_to_frontier(self.start, 0)

        while not self.frontier.is_empty():

            state = self.frontier.pop()

            # Priority queues contain tuples:
            # (priority, word)
            if isinstance(state, tuple):
                state = state[1]

            # Skip a word if we have already explored it.
            if state in self.explored:
                continue

            self.explored.add(state)

            self.current_state = state

            # If we reached the goal, return the path.
            if state == self.goal:
                return self.paths[state]

            # Find all valid one-letter neighbors.
            neighbors = get_neighbors(
                state,
                neighbor_index
            )

            for neighbor in neighbors:

                if neighbor not in self.paths: # only add a neigbor first time we discover it

                    # Store the path used to reach this neighbor.
                    self.paths[neighbor] = (
                        self.paths[state] + [neighbor]
                    )

                    # Let the specific algorithm decide
                    # how the neighbor enters the frontier.

                    cost = get_cost(neighbor)



                    #cost = get_cost(
                    #    neighbor,
                    #    self.data
                    #)

                    self.add_to_frontier(
                        neighbor,
                        cost
                    )

        return None

    def add_to_frontier(self, neighbor, cost):
        """
        Default behavior for BFS and DFS.

        BFS and DFS do not use word cost to decide
        which node to explore next.
        """

        self.frontier.add(neighbor)


class BFS(SearchAlgorithm):
    """Breadth-First Search."""

    def __init__(self, start, goal, dictionary, data):

        # BFS uses a Queue.
        super().__init__(
            start,
            goal,
            dictionary,
            data,
            f.Queue()
        )



class UCS(SearchAlgorithm):
    """Uniform Cost Search."""

    def __init__(self, start, goal, dictionary, data):

        # UCS uses a PriorityQueue.
        super().__init__(
            start,
            goal,
            dictionary,
            data,
            f.PriorityQueue()
        )

        # Cost of reaching each word from the start.
        self.cost = {
            start: 0
        }

    def add_to_frontier(self, neighbor, cost):

        # Calculate the cost of reaching this neighbor.
        if neighbor == self.start:
            self.frontier.add(
                (0, neighbor)
            )
            return

        new_cost = (
            self.cost[self.current_state]
            + cost
        )

        # Only update if this is a cheaper path.
        if (
            neighbor not in self.cost
            or new_cost < self.cost[neighbor]
        ):

            self.cost[neighbor] = new_cost

            # PriorityQueue requires:
            # (priority, state)
            self.frontier.add(
                (new_cost, neighbor)
            )


if __name__ == "__main__":

    test_cases = [
        ("COLD", "WARM"),
        ("SHOPPING", "TRACKING"),
        ("UNREASONABLE", "UNSEASONABLY"),
        ("AND", "AAL"),
        ("THAT", "ABEL"),
        ("AAHED", "WATER"),
        ("AAHED", "THERE"),
        ("LITTLE", "MIDDLE"),
        #("OCEAN ", "BEGAN")
        ("ZOOMS", "THYME")
        
    ]

    print("\nWORD MORPH TEST CASES")

    for start, goal in test_cases:

        print("\n" + start, "->", goal)

        # -------------------------
        # BFS
        # -------------------------

        bfs = BFS(
            start,
            goal,
            dictionary,
            data
        )

        start_time = time.perf_counter()

        bfs_path = bfs.search()
        bfs_time = time.perf_counter() - start_time

        if bfs_path is None:

            print("BFS: No path found")

        else:

            bfs_cost = 0

            for word in bfs_path[1:]:
                bfs_cost += get_cost(
                    word
                )

            print("BFS")
            print(
                "Path:",
                " -> ".join(bfs_path)
            )
            print(
                "Steps:",
                len(bfs_path) - 1
            )
            print(
                "Cost:",
                bfs_cost
            )
            print("Time:", bfs_time, "seconds")

        # -------------------------
        # UCS
        # -------------------------

        ucs = UCS(
            start,
            goal,
            dictionary,
            data
        )

        start_time = time.perf_counter()

        ucs_path = ucs.search()
        ucs_time = time.perf_counter() - start_time

        if ucs_path is None:

            print("UCS: No path found")

        else:

            print("UCS")
            print(
                "Path:",
                " -> ".join(ucs_path)
            )
            print(
                "Steps:",
                len(ucs_path) - 1
            )
            print(
                "Cost:",
                ucs.cost[goal]
            )
            print("Time:", ucs_time, "seconds")

    
# MINI-DICTIONARY DEAD-END TEST

mini_dictionary = {
    "PIG",
    "PIT",
    "FIG",
    "FOG",
    "COG",
    "COW"
}

mini_costs = {
    "PIG": 4,
    "PIT": 5,
    "FIG": 6,
    "FOG": 5,
    "COG": 6,
    "COW": 5
}

mini_neighbor_index = defaultdict(set)

for word in mini_dictionary:
    for i in range(len(word)):
        pattern = word[:i] + "_" + word[i+1:]
        mini_neighbor_index[pattern].add(word)

# Save the original values
original_dictionary = dictionary
original_cost_of = cost_of
original_neighbor_index = neighbor_index

# Use mini versions
dictionary = mini_dictionary
cost_of = mini_costs
neighbor_index = mini_neighbor_index

print("\nMINI-DICTIONARY DEAD-END TEST")

bfs = BFS("PIG", "COW", dictionary, data)
bfs_path = bfs.search()

print("BFS")
print("Path:", " -> ".join(bfs_path))
print("Steps:", len(bfs_path) - 1)
print("Cost:", sum(get_cost(word) for word in bfs_path[1:]))

ucs = UCS("PIG", "COW", dictionary, data)
ucs_path = ucs.search()

print("UCS")
print("Path:", " -> ".join(ucs_path))
print("Steps:", len(ucs_path) - 1)
print("Cost:", sum(get_cost(word) for word in ucs_path[1:]))

dictionary = original_dictionary
cost_of = original_cost_of
neighbor_index = original_neighbor_index


print("PIG -> COW")