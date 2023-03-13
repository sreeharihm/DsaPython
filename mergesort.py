def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left,right)

def merge(left,right):
    result =[]
    i=0
    j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result += left[i:]
    result += right[j:]
    return result

print(merge_sort([3,6,8,10,1,2,1]))

"""
    left- [3,6,8]
        left- [3]
        right-[6,8]
            left-[6]
            right-[8]
        left-[3,6,8]
    right- [10,1,1,2]
        left-[10]
        right-[1,1,2]
            left-[1]
            right-[1,2]
    right-[1,1,2,10]

    result -[1,1,2,3,6,8,10]

"""