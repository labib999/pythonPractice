
toDoList = []

def show():
    print("Showing all the task:")
    for index,item in enumerate(toDoList, start = 1):
        print(index,item)
    print()

def add():
    toDoList.append(input("Add new task: "))
    show()

def remove():
    while True:
        try:
            index = int(input("what to remove? Please enter the index: "))
            if 1 <= index <= len(toDoList) - 1:
                toDoList.pop(index - 1)
                show()
                break
            else:
                print("Out of range for numbers of tasks")
        except:
            print("Please enter a valid input")
def main():
    while True:
        a = int(input("1. Add task \n"
                    "2. Delete task with number\n" \
                    "3. Show all tasks\n"
                    "4. Close\n"))
        
        if a == 1:
            add()
        elif a == 2:
            remove()
        elif a == 3:
            show()
        elif a == 4:
            break

main()