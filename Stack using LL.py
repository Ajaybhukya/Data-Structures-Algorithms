#Implemtation of Stack using Linked List
class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
class Stack:
    def __init__(self):
        self.top=None
    def push(self,data):
        if self.top is None:
            self.top=Node(data)
            return
        self.top=Node(data,self.top)
    def pop(self):
        if self.top is None:
            print("Stack is Empty")
            return None
        if self.top.next is None:
            self.top=None
        else:
            self.top=self.top.next
    def display(self):
        if self.top is None:
            print("Stack is Empty")
            return
        itr=self.top
        while itr is not None:
            print(itr.data,end=' ')
            itr=itr.next
    def length_of_stack(self):
        count=0
        itr = self.top
        while itr is not None:
            count+=1
            itr = itr.next
        return count
S=Stack()
print("Welcome to our Stack")
while True:
   try:
    print()
    print("Select an option:")
    print("1.Push")
    print("2.Pop")
    print("3.Display")
    print("4.Length of Stack")
    print("5.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        data=int(input("Enter data:"))
        S.push(data)
        S.display()
        print()
    elif choice==2:
        S.pop()
        S.display()
        print()
    elif choice==3:
        S.display()
        print()
    elif choice==4:
        print(f'Length of Stack is {S.length_of_stack()}')
    elif choice==5:
        print("Thank You for using our Stack")
        break
    else:
        print("Wrong Choice")
        print("Please enter correct choice")
   except:
    print("Wrong Choice")
    print("Please enter correct choice")