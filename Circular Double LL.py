class Node:
    def __init__(self,data,prev=None,next=None):
        self.data=data
        self.prev=prev
        self.next=next
class CircularDLL:
    def __init__(self):
        self.head=self.tail=None
    def insert_at_beginning(self,data):
        if self.head is None:
            self.head=self.tail=Node(data)
            self.tail.next=self.head
            self.tail.prev=self.head
            return
        node=Node(data,None,self.head)
        self.head.prev=node
        self.head=node
        self.head.prev=self.tail
        self.tail.next=self.head
    def insert_at_end(self,data):
        if self.head is None:
            self.head=self.tail=Node(data)
            self.tail.next=self.head
            self.tail.prev=self.head
            return
        node=Node(data,self.tail,self.head)
        self.tail.next=node
        self.tail=node
        self.head.prev=self.tail
    def insert_at_position(self,pos,data):
        if pos<0 or pos>self.length_of_list():
            print("Invalid Index")
            return
        elif pos==1:
            self.insert_at_beginning(data)
        else:
            itr=self.head
            count=1
            while count!=pos-1:
                count+=1
                itr=itr.next
            node=Node(data,itr,itr.next)
            itr.next.prev=node
            itr.next=node
    def delete_at_beginning(self):
        if self.head is None:
            print("Empty List")
            return
        if self.head.next==self.head:
            self.head=self.tail=None
        else:
            self.head=self.head.next
            self.head.prev=self.tail
            self.tail.next=self.head
    def delete_at_end(self):
        if self.tail.next is self.head:
            self.head=self.tail=None
        else:
            itr=self.head
            while itr.next.next is not self.head:
                itr=itr.next
            itr.next=self.head
            self.tail=itr
            self.head.prev=self.tail
    def delete_at_position(self,pos):
        if pos<0 or pos>self.length_of_list():
            print("Empty List")
            return
        if pos==1:
            L.delete_at_beginning()
        else:
            itr=self.head
            count=1
            while count!=pos-1:
                count+=1
                itr=itr.next
            if itr.next.next is self.head:
                itr.next=self.head
                self.tail=itr
                self.head.prev=self.tail
            else:
                itr.next=itr.next.next
                itr.next.prev=itr
    def length_of_list(self):
        itr=self.head
        count=1
        while itr.next!=self.head:
            count+=1
            itr=itr.next
        return count
    def forward_traversal(self):
        if self.head is None:
            print("Empty List")
            return
        print("Forward Traversal:",end='')
        itr=self.head
        print(itr.data,end='-->')
        itr=itr.next
        while itr!=self.head:
            print(itr.data,end='-->')
            itr=itr.next
    def backward_traversal(self):
        if self.head is None:
            print("Empty List")
            return
        print("Backward Traversal:",end='')
        itr=self.tail
        print(itr.data,end='-->')
        itr=itr.prev
        while itr!=self.tail:
            print(itr.data,end='-->')
            itr=itr.prev
L=CircularDLL()
while True:
   try:
    print()
    print("1. Insert At Beginning")
    print("2. Insert At End")
    print("3. Insert At Position")
    print("4. Delete At Beginning")
    print("5. Delete At End")
    print("6.Delete At Position")
    print("7. Forward Traversal")
    print("8. Backward Traversal")
    print("9. Length of List")
    print("10. Exit")
    ch=int(input("Enter Your Choice:"))
    if ch==1:
        L.insert_at_beginning(int(input("Enter Data:")))
        L.forward_traversal()
        print()
        L.backward_traversal()
        print()
    elif ch==2:
        L.insert_at_end(int(input("Enter Data:")))
        L.forward_traversal()
        print()
        L.backward_traversal()
        print()
    elif ch==3:
        L.insert_at_position(int(input("Enter Position:")),int(input("Enter Data:")))
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
        L.delete_at_position(int(input("Enter Position:")))
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
        print(f'Length of List: {L.length_of_list()}')#or print(L.length_of_list())
    elif ch==10:
        print("Thank You for using Circular Double Linked List")
        break
    else:
        print("Invalid Choice")
        print("Re-enter your choice")
   except:
        print("Invalid Input")
        print("Re-enter your choice")