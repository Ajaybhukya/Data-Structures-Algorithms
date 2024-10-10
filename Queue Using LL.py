class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
class Queue:
    def __init__(self):
        self.first=self.last=None
    def Enqueue(self,data):
        if self.first is None:
            self.first=self.last=Node(data)
            return
        node=Node(data)
        self.last.next=node
        self.last=node
    def Dequeue(self):
        if self.first is None:
            print("Empty Queue")
            return
        if self.first.next is None:
            self.first=self.last=None
        else:
            self.first=self.first.next
    def display(self):
        if self.first is None:
            print("Empty Queue")
            return 0
        itr=self.first
        while itr is not None:
            print(itr.data,end=' ')
            itr=itr.next
    def length_of_queue(self):
        if self.first is None:
            print("Empty Queue")
            return 0
        itr=self.first
        count=0
        while itr is not  None:
            count+=1
            itr=itr.next
        return count
Q=Queue()
print("Welcome to Queue")
while True:
    print()
    print("Enter your choice:")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Length of Queue")
    print("5. Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        data=int(input("Enter the data: "))
        Q.Enqueue(data)
        Q.display()
        print()
    elif choice==2:
        Q.Dequeue()
        Q.display()
        print()
    elif choice==3:
        Q.display()
        print()
    elif choice==4:
        print("Length of Queue is: ",Q.length_of_queue())
    elif choice==5:
        print("Thank you for using our Queue")
        break
    else:
        print("Invalid Choice")
        print("Re-entry the choice")