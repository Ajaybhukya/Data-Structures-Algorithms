def selection_sort(arr):
    for i in range(len(arr)):
        min_index=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr
values=[int(x) for x in input("Enter the elements  with single Spaces: ").split()]
result=selection_sort(values)
print("After selectiion Sort")
for i in result:
    print(i,end=' ')