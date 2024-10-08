#liked list using python
l=[]
mx=3
top=-1
while True:
 print("\nMENU")
 print("1.push")
 print("2.pop")
 print("3.display")
 print("4.exit")
 ch=int(input("Read your choices\n"))
 if ch==1:
  i=1
  while i==1:
   if(top==mx-1):
    print("stack is overflow") 
   else:
    l.append(int(input("read a value\n")))
    top+=1
   i=int(input("Do you want to continue\n"))
 elif ch==2:
  if top==-1:
   print("Stack is underflow")
  else:
   print("poped element is ",l.pop())
   top-=1
 elif ch==3:
  n=len(l)
  for i in range(n-1,-1,-1):
   print(l[i],end=" ")
 else: 
  print("thank you")
  break;