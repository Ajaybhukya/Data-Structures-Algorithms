values=[int(x) for x in input("Enter the elements with single spaces:").split()]
def binary_search(low,ele,high):
    if low<=high:
        mid=(low+high)//2
        if ele==values[mid]:
            return (mid+1)
        elif ele<values[mid]:
            high=mid-1
            return binary_search(low,ele,high)
        else:
            low=mid+1
            return binary_search(low,ele,high)
ele=int(input("Enter the element to search:"))
position=binary_search(0,ele,len(values)-1)
if position is not  None:
    print(f"Element found at {position} position")
else:
    print("No such element")
