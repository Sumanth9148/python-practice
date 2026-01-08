def bubble(arr):
    n=len(arr)

    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

    print(arr)

ar=[13,46,24,52,20,9]
bubble(ar) 
