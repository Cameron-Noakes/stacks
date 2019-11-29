# Non-primitve data types - Stacks
# 1 pointer to top
# works with only 64-bit Python

x = 1
state = True
stack = []

pointer = -1

def add():
    global pointer
    value_to_add = input("Enter value to add onto stack: (0 to stop): ")
    stack.append(value_to_add)
    pointer +=1
    while value_to_add != 0:
        value_to_add = input("Enter value to add onto stack: (0 to stop): ")
        pointer +=1
        stack.append(value_to_add)
        if value_to_add == "0":
            stack.pop()
            pointer -=1
            return pointer
            



def pop():
    global pointer
    if pointer == 0:
        print ("Stack is empty, cannot pop from empty stack.")
    else:
        
        stack.pop()
        
        pointer -=1
        print ("Item popped!")
    

def read():
    global pointer
    print ("pointer is at: "+pointer+",Stack:",stack)
    

def __main__():
    print ("Stack:",stack, "pointer is at:", pointer)
    menu = input("Would you like to add, pop or read the stack?: (a,p,r): ")
    if menu == "a":
        add()

    elif menu == "p":
        pop()

    elif menu == "r":
        read()

    else:
        
        print ("That is not a valid input. Please try again.")

while state == True:
    print ("\n")
    __main__()
