def select_sort(arr):
    n=len(arr)

    for i in range(n-1):
        min=i
        for j in range(i+1,n):
            if arr[j]<arr[min]:
                min=j

        arr[i],arr[min]=arr[min],arr[i]

    print(arr)


ar=[13,46,24,52,20,9]
select_sort(ar)


