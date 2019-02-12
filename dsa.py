def biSearch(li, x, low, high):
    """this is binary search tree"""
    # if high - low < 2:
    #     return li[low] == x or li[high] == x
    mid = int((low + high) / 2)  #low + int((high - low)/2)

    if low == mid or low == high:
        return li[low] == x or li[high] == x

    if li[mid] == x:
        return True
    elif li[mid] > x:
        return biSearch(li, x, low, mid)
    elif li[mid] < x:
        return biSearch(li, x, mid, high)

def selectionSort(li):
    """selection sort"""
    for i in range(0,len(li)):
        for j in range(0,len(li)):
            if li[i] < li[j]:
                li[i], li[j] = li[j], li[i]
    print li


def bubbleSort(li):
    """bubble sort"""
    for i in range(0, len(li)):
        for j in range(0, len(li) - i - 1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
    print li


def insertionSort(li):
    """insertion sort"""
    for i in range(1, len(li)):
        temp = li[i]
        for j in range(i-1, -1, -1):
            if temp < li[j]:
                li[j+1], li[j] = li[j], li[j+1]

    print li


def shellSort(li):
    """shell sort"""
    gap = int(len(li) / 2)

    while gap > 0:

        for i in range(gap):

            for j in range(i + gap, len(li), gap):

                for k in range(j, -1, -gap):

                    if li[k] > li[j]:
                        li[k], li[j] = li[j], li[k]


        gap = int(gap / 2)


    print li


def merge(left, right):
    i,j =0,0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i +=1
        else:
            result.append(right[j])
            j +=1

    if i < len(left):
        for k in range(i, len(left)):
            result.append(left[k])

    if j < len(right):
        for k in range(j, len(right)):
            result.append(right[k])

    return result

def mergeSort(li):
    """merge sort"""

    #print li

    if len(li) < 2:
        return li[:]
    else:
        mid = int ( len(li) / 2)
        left = mergeSort(li[:mid])
        right = mergeSort(li[mid:])
        return merge(left, right)



if __name__ == "__main__":

    li = [45, 56, 12, 5, 78, 123, 647, 1, 45, 3, 21]

    # li.sort()
    # fi = biSearch(li, 67, 0, len(li))
    # print fi

    #selectionSort(li)

    #bubbleSort(li)

    #insertionSort(li)

    #shellSort(li)

    lk = mergeSort(li)

    print lk
