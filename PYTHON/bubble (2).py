#arr=[1,2,3,4,5,6,7,8,9]
arr=[9,44,67,4,7,2,6,45,23,67]
print(arr)
print(len(arr))
def bubble():
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if(arr[j]>arr[j+1]):
                t=arr[j+1]
                arr[j+1]=arr[j]
                arr[j]=t
bubble()                
print(arr)               