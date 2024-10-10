values=[int(x) for x in input("Enter the elements with single white space: ").split()]
def bubble_sort(arr):
    n=len(arr)
    for i in range(n-1):
        for  j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
sorted_arr=bubble_sort(values)
for i in sorted_arr:
    print(i,end=' ')