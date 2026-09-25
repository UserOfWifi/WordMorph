import csv
import frontiers as f
#This is currently just an experiment to see if git hub works.
#Once everything is set these comments can be removed
print("Hello World!")
x = 21
print("What is %i when divided by %i?" "\nIt's %i!!" % (x, x/3, x/7)) 
# Testing gihub pushing

if __name__ == "__main__":
    print("hello")       
    my_stack = f.Stack() # creating stack 
    print("Stack Made")

    my_stack.add("hello")
    print("Hello added to stack")

    my_stack.add("How")
    my_stack.add("are")
    my_stack.add("you")
    print("'How, are, you' added to stack")

    while not my_stack.is_empty(): # remove items from stack
        print(my_stack.pop())
    print("Stack is empty")

    my_queue = f.Queue() # creating stack 
    print("Queue Made")

    my_queue.add("hello")
    print("Hello added to queue")

    my_queue.add("How")
    my_queue.add("are")
    my_queue.add("you")
    print("'How, are, you' added to stack")

    while not my_queue.is_empty(): # remove items from stack
        print(my_queue.pop())
    print("Queue is empty")
    print("\n\n")
    with open('WordMorphText.csv', mode='r') as WM:
        reader = csv.DictReader(WM)
        firstRow = next(reader)
        print("Column Names: ", firstRow)
        # for row in reader: # This prints all rows, it takes a while
        #     print("Column Names: ", row)
