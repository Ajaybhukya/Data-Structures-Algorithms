class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
        self.head=None
    def insert_at_beginning(self,data):
        if self.head==None:
            self.head=Node(data,None)
            return
        self.head=Node(data,self.head)
    def insert_at_end(self,data):
        if self.head==None:
            self.head=Node(data,None)
            return
        itr=self.head
        while itr.next is not None:
            itr=itr.next
        itr.next=Node(data)
    def insert_at_position(self,pos,data):
        if self.head==None:
            print("Empty List")
            return
        if pos<1 or pos>self.length_of_list():
            print("Invalid Index")
        elif pos==1:
            self.insert_at_beginning(data)
        else:
            itr=self.head
            count=1
            while count!=pos-1:
                count+=1
                itr=itr.next
            itr.next=Node(data,itr.next)
    def delete_at_beginnig(self):
        if self.head is None:
            print("Empty LinkedList")
            return
        self.head=self.head.next
    def delete_at_end(self):
        if self.head is None:
            print("Empty LinkedList")
            return
        itr=self.head
        while itr.next.next is not None:
            itr=itr.next
        itr.next=None
    def delete_at_position(self,pos):
        if self.head==None:
            print("Empty List")
            return
        if pos<1 or pos>self.length_of_list():
            print("Invalid Index")
        elif pos==1:
            self.delete_at_beginnig()
        else:
            itr=self.head
            count=1
            while count!=pos-1:
                count+=1
                itr=itr.next
            itr.next=itr.next.next
    def display(self):
        if self.head is None:
            print("Empty LinkedList")
            return
        itr=self.head
        while itr is not None:
            print(itr.data,'->',end='')
            itr=itr.next
    def length_of_list(self):
        len=0
        itr=self.head
        while itr is not  None:
            len+=1
            itr=itr.next
        return  len
L=LinkedList()
while True:
    print('1.Insert at beginning')
    print('2.Insert at end')
    print('3.Insert at position')
    print('4.Delete at beginning')
    print('5.Delete at end')
    print('6.Delete at position')
    print('7.Display')
    print('8.Length of list')
    print('9.Exit')
    ch=int(input('Enter your choice:'))
    if ch==1:
        data=int(input("Enter data:"))
        L.insert_at_beginning(data)
        L.display()
        print()
    elif ch==2:
        data=int(input("Enter data:"))
        L.insert_at_end(data)
        L.display()
        print()
    elif ch==3:
        data=int(input("Enter data:"))
        pos=int(input("Enter position:"))
        L.insert_at_position(pos,data)
        L.display()
        print()
    elif ch==4:
        L.delete_at_beginnig()
        L.display()
        print()
    elif ch==5:
        L.delete_at_end()
        L.display()
        print()
    elif ch==6:
        pos=int(input("Enter position:"))
        L.delete_at_position(pos)
        L.display()
        print()
    elif ch==7:
        L.display()
        print()
    elif ch==8:
        print(f'Length of list is {L.length_of_list()}')
        print()
    elif ch==9:
        print("Thank you")
        break
    else:
        print("Invalid Choice")
