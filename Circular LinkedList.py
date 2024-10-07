class Node:
    def __init__(self, data=None,next=None):
        self.data = data
        self.next = next
class CircularLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def insert_at_beginning(self,data):
        if self.head is None:
            self.head=self.tail=Node(data)
            self.tail.next=self.head
            return
        self.head=Node(data,self.head)
        self.tail.next=self.head
    def insert_at_end(self,data):
        if self.head is None:
            self.head = self.tail = Node(data)
            self.tail.next = self.head
            return
        node=Node(data)
        self.tail.next=node
        self.tail=node
        self.tail.next=self.head
    def insert_at_position(self,pos,data):
        if pos<0 or pos>self.length_of_list():
            print("Empty LinkedList")
            return
        if pos==1:
            self.insert_at_beginning(data)
        else:
            itr=self.head
            count=1
            while count!=pos-1:
                count+=1
                itr=itr.next
            itr.next=Node(data,itr.next)
    def delete_at_begining(self):
        if self.head is None:
            print("Empty Linked List")
            return
        self.head=self.head.next
        self.tail.next=self.head
    def delete_at_end(self):
        if self.head is None:
            print("Empty list")
            return
        if self.head.next is self.head:
            self.head=None
            return
        itr=self.head
        while itr.next.next is not self.head:
            itr=itr.next
        itr.next=self.head
        self.tail=itr
    def delete_at_positin(self,pos):
        if pos<0 or pos>self.length_of_list():
            print("Invalid index")
            return
        if pos==1:
            self.delete_at_begining()
            return
        else:
            itr=self.head
            count=1
            while count!=pos-1:
                count+=1
                itr=itr.next
            itr.next=itr.next.next
    def length_of_list(self):
        itr=self.head
        count=1
        while itr.next!=self.head:
            count+=1
            itr=itr.next
        return count
    def display(self):
        if self.head is None:
            print("Empty LinkedList")
            return
        itr=self.head
        print(itr.data,'->',end='')
        itr=itr.next
        while itr!=self.head:
            print(itr.data,'->',end='')
            itr=itr.next
L=CircularLinkedList()
while True:
    try:
        print("\n1. Insert at beginning\n2. Insert at end\n3. Insert at position\n4. Delete at beginning\n5. Delete at end\n6. Delete at position\n7. Display\n8. Length of list\n9. Exit")
        ch=int(input("Enter your choice: "))
        if ch==1:
            L.insert_at_beginning(int(input("Enter data: ")))
            L.display()
            print()
        elif ch==2:
            L.insert_at_end(int(input("Enter data: ")))
            L.display()
            print()
        elif ch==3:
            L.insert_at_position(int(input("Enter position: ")),int(input("Enter data: ")))
            L.display()
            print()
        elif ch==4:
            L.delete_at_begining()
            L.display()
            print()
        elif ch==5:
            L.delete_at_end()
            L.display()
            print()
        elif ch==6:
            L.delete_at_positin(int(input("Enter position: ")))
            L.display()
            print()
        elif ch==7:
            L.display()
            print()
        elif ch==8:
            print(f'Length of list: {L.length_of_list()}')
        elif ch==9:
            print("Thanks for using Circular Linked List")
            break
        else:
            print("Invalid Choice")
            print("Re-enter your choice")
    except:
        print("Invalid Input")
        print("Enter Correct Choice")
