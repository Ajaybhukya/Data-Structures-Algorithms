from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, data):
        self.container.append(data)

    def pop(self):
        if not self.container:
            return "Empty Stack"
        else:
            return self.container.pop()

    def top(self):
        if not self.container:
            return "Empty stack"
        else:
            return self.container[-1]

    def display(self):
        if not self.container:
            return "Empty stack"
        for i in reversed(self.container):
            print(i, end=' ')
        print()
    def size(self):
        return len(self.container)
S = Stack()
print("Welcome to Stack")
while True:
   try:
    print("select your choice")
    print("1. Push")
    print("2. Pop")
    print("3. Top")
    print("4. Display")
    print("5. Size")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        data = int(input("Enter data: "))
        S.push(data)
        S.display()
    elif choice == 2:
        data = S.pop()
        if data == "Empty Stack":
            print("Stack is empty")
        else:
            print("Popped data: ", data)
            S.display()
    elif choice == 3:
        data = S.top()
        if data == "Empty Stack":
            print("Stack is empty")
        else:
            print("Top data: ", data)
    elif choice == 4:
        S.display()
    elif choice == 5:
        print("Size of stack: ", S.size())
    elif choice == 6:
        print("Thank you for using the stack")
        break
    else:
        print("Invalid choice")
        print('Re-enter your choice')
   except ValueError:
    print("Invalid input")
    print('Re-enter your choice')