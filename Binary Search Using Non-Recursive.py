l=[int(x) for x in input("Enter the elements with single spaces:").split()]
l.sort()
print("After sorting the elements are:")
for i in l:
    print(i,end=' ')
print()
ele=int(input("Enter the element to search:"))
low=0
high=len(l)-1
mid=0
flag=0
while low<=high:
    try:
        mid=(low+high)//2
        if ele==l[mid]:
            print(f'Element Found at position:{mid+1}')
            flag=1
            break
        elif ele<l[mid]:
            high=mid-1
        elif ele>l[mid]:
            low=mid+1
    except:
        print("Invalid Input!!re-enter")
if flag==0:
    print("No Such Element Found")
