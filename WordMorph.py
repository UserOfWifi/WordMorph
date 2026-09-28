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

    from search import BFS, DFS, UCS, GreedyBestFirst, AStar

    # print("hello")       
    # my_stack = f.Stack() # creating stack 
    # print("Stack Made")

    # my_stack.add("hello")
    # # print("Hello added to stack")

    # my_stack.add("How")
    # my_stack.add("are")
    # my_stack.add("you")
    # # print("'How, are, you' added to stack")

    # while not my_stack.is_empty(): # remove items from stack
    #     print(my_stack.pop())
    # print("Stack is empty")

    # my_queue = f.Queue() # creating stack 
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
    # print("\n\n")

    # validWords = list()
    # userStartWord = "COLD" #Ensure to use .lower()
    # userEndWord = "warm"
    # entireWM = pandas.read_csv('WordMorphText.csv', keep_default_na=False) #Had to add this cause SOMEWHERE there is a null/NaN value
    # certainLength = entireWM[entireWM["length"] == len(userStartWord.lower())] #Instantly grabs all same length words without looping, efficient!
    # print(certainLength)
    # wordCol = certainLength.columns[0] #Speicifically looks at the word colum

    # for word, cost in zip(certainLength[wordCol], certainLength["Cost"]):
    #     #print("This is 'word': ", word)
    #     diffs = 0
    #     for x, y in zip(userStartWord.lower(), word):
    #         if x!=y:
    #             diffs += 1
    #             if diffs>=2:
    #                 diffs = 0
    #                 break
    #     if diffs == 1:
    #         diffs = 0 #Reset back for userEndWord
    #         #print("|/|/|/|/|/|/|/|/| FIRST START")
    #         validWords.append((word, cost))
    # print(validWords)

    wording = WordMorph("blistering", "stuttering")
    startTime = time.time()

    Breathe = BFS(wording)
    bResult = Breathe.search()
    print("BFS: ", bResult)
    print(f"Finished in {time.time() - startTime:.2f} seconds")

    # with open("WordMorphText.csv", mode='r') as WM:
    #     reader = csv.DictReader(WM)
    #     firstRow = next(reader)
    #     print("Column Names: ", firstRow)
        # for row in reader: # This prints all rows, it takes a while
        #     print("Column Names: ", row)
