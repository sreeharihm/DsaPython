def quicksort(arr):
    if len(arr)<=1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x<pivot]
    middle = [x for x in arr if x==pivot]
    right = [x for x in arr if x>pivot]
    return quicksort(left)+middle + quicksort(right)

print(quicksort([3,6,8,10,1,2,1]))

"""
Quick Sort(P-P-D)Pivot Partition Divide 
1st Pass:
    pivot -10
    left - [3,6,8,1,2,1]
    middle -[10]
    right- []
    return Q([3,6,8,1,2,1])+[10]
2nd Pass:
    pivot - 8
    left -[3,6,1,2,1]
    middle -[8]
    right- []
    return Q([3,6,1,2,1])]+[8]+[]
3rd Pass:
    pivot -1
    left-[]
    middle -[1,1]
    right-[3,6,2]
    return Q([])+[1,1]+Q([3,6,2])

Last step: [1,1]+[2]+[3]+[6]+[8]+[10]
Output: [1,1,2,3,6,8,10]
"""