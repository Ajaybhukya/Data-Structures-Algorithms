class Node:
    def __init__(self, data=None,prev=None,next=None):
        self.data = data
        self.prev = prev
        self.next = next
class DoubleLinkedList:
    def __init__(self):
        self.tail=self.head=None
    def insertion_at_beginning(self,data):
        if self.head is None:
            self.tail=self.head=Node(data)
            return
        node=Node(data,None,self.head)
        # node.next=self.head
        self.head.prev=node
        self.head=node
    def insert_at_end(self,data):
        if self.head is None:
            self.tail=self.head=Node(data)
            return
        node=Node(data,self.tail,None)
        self.tail.next=node
        self.tail=node
        # node.prev=self.tail
    def length_of_list(self):
        itr=self.head
        count=0
        while  itr is not  None:
            count+=1
            itr=itr.next
        return count
    def insert_at_position(self,pos,data):
        if pos<0 or pos>self.length_of_list():
            print("Invalid Index")
            return
        if pos==1:
            L.insertion_at_beginning(data)
        else:
            itr=self.head
            count=1
            while count!=pos-1:
                count+=1
                itr=itr.next
            node=Node(data)
            node.next=itr.next
            itr.next.prev=node
            itr.next=node
            node.prev=itr
    def delete_at_beginning(self):
        if self.head is None:
            print("List is Empty")
            return
        self.head=self.head.next
        self.head.prev=None
    def delete_at_end(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head=self.tail=None
            return
        itr=self.head
        while itr.next.next is not  None:
            itr=itr.next
        itr.next=None
        self.tail=itr
    def delete_at_position(self,pos):
        if pos<0 or pos>self.length_of_list():
            print("Invalid Index")
        elif pos==1:
            self.delete_at_beginning()
        else:
            itr=self.head
            count=1
            while count!=pos-1:
                count+=1
                itr=itr.next
            if itr.next.next is None:
                itr.next=None
                self.tail=itr
            else:
                itr.next=itr.next.next
                itr.next.prev=itr

    def forward_traversal(self):
        print("Forward Traversal:",end='')
        itr=self.head
        while itr is not None:
            print(itr.data,end='-->')
            itr=itr.next
    def backward_traversal(self):
        print("Backward Traversal:",end='')
        itr=self.tail
        while itr is not None:
            print(itr.data,end='-->')
            itr=itr.prev
L=DoubleLinkedList()
while True:
   try:
    print()
    print("1.Insertion at beginning")
    print("2.Insertion at end")
    print("3.Insertion at position")
    print("4.Delete at beginning")
    print("5.Delete at end")
    print("6.Delete at position")
    print("7.Forward traversal")
    print("8.Backward traversal")
    print("9.Length of list")
    print("10.Exit")
    ch=int(input("Enter your choice:"))
    if ch==1:
        data=int(input("Enter data:"))
        L.insertion_at_beginning(data)
        L.forward_traversal()
        print()
        L.backward_traversal()
        print()
    elif ch==2:
        data=int(input("Enter data:"))
        L.insert_at_end(data)
        L.forward_traversal()
        print()
        L.backward_traversal()
        print()
    elif ch==3:
        data=int(input("Enter data:"))
        pos=int(input("Enter position:"))
        L.insert_at_position(pos,data)
        L.forward_traversal()
        print()
        L.backward_traversal()
        print()
    elif ch==4:
        L.delete_at_beginning()
        L.forward_traversal()
        print()
        L.backward_traversal()
        print()
    elif ch==5:
        L.delete_at_end()
        L.forward_traversal()
        print()
        L.backward_traversal()
        print()
    elif ch==6:
        pos=int(input("Enter position:"))
        L.delete_at_position(pos)
        L.forward_traversal()
        print()
        L.backward_traversal()
        print()
    elif ch==7:
        L.forward_traversal()
        print()
    elif ch==8:
        L.backward_traversal()
        print()
    elif ch==9:
        print(f'Length of list is {L.length_of_list()}')
    elif ch==10:
        print('Thank you for using the Double Linked List')
        break
    else:
        print("Invalid choice")
        print("Enter your choice again")
   except :
       print("Invalid input!")
       print("Re-enter your choice")