#RUN THIS IN THE GIT TERMINAL
import pandas
import time #Thought this would be nice
class WordMorph:
    def __init__(self, starter, ender):
        self.start = starter
        self.goal = ender

    def neighbors(self, state):
        validWords = []
        entireList = pandas.read_csv('WordMorphText.csv', keep_default_na=False) #Had to add this cause SOMEWHERE there is a null/NaN value
        setLength = entireList[entireList["length"] == len(state.lower())] #Instantly grabs all same length words without looping, efficient!
        #print(setLength)
        wordCol = setLength.columns[0] #Speicifically looks at the word colum
    
        for word, cost in zip(setLength[wordCol], setLength["Cost"]):
            #print("This is 'word': ", word)
            diffs = 0
            for x, y in zip(state.lower(), word):
                if x!=y:
                    diffs += 1
                    if diffs>=2:
                        diffs = 0
                        break
            if diffs == 1:
                diffs = 0 #Reset back for userEndWord
                #print("|/|/|/|/|/|/|/|/| FIRST START")
                validWords.append((word, cost))
        return sorted(validWords)

if __name__ == "__main__":
    # from search import BFS, DFS, UCS, GreedyBestFirst, AStar
    from search import BFS, UCS

    test_cases = [
        # ("goat", "barn")
        ("and", "aal"),
        ("cold", "warm"),
        ("that", "abel"),
        ("aahed", "water"),
        ("aahed", "there"),
        ("zooms", "thyme"),
        # ("danger", "hoping"),
        ("little", "middle"),
        # ("selling", "sounded"),
        # ("muttering", "withering"),
        # ("blistering", "stuttering"),
        # ("nationalism", "rationalize"),
        ("unreasonable", "unseasonably")
    ]
    for start, goal in test_cases:

        wording = WordMorph(start, goal)
        startTime = time.time()

        print(f"\nWord morph selected: [{start} -> {goal}]")
        Breathe = BFS(wording)
        bResult = Breathe.search()
        print("BFS: ", bResult)
        print(f"Path Length: {len(bResult[0])}")
        print(f"Finished in {time.time() - startTime:.2f} seconds\n")

        startTime = time.time()

        Uniform = UCS(wording)
        uResult = Uniform.search()
        print("UCS: ", uResult)
        print(f"Path Length: {len(uResult[0])}")
        print(f"Finished in {time.time() - startTime:.2f} seconds\n---")

    # with open("WordMorphText.csv", mode='r') as WM:
    #     reader = csv.DictReader(WM)
    #     firstRow = next(reader)
    #     print("Column Names: ", firstRow)
        # for row in reader: # This prints all rows, it takes a while
        #     print("Column Names: ", row)
