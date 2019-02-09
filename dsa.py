def biSearch(li, x, low, high):
    """this is binary search tree"""
    if high - low < 2:
        return li[low] == x or li[high] == x

    mid = low + int((high - low )/2)

    if li[mid] == x:
        return True
    elif li[mid] > x:
        return biSearch(li, x, low, mid - 1)
    elif li[mid] < x:
        return biSearch(li, x, mid + 1, high)




if __name__ == "__main__":

    li = [45, 56, 12, 5, 78, 123, 647, 1, 45, 3, 21]
    li.sort()
    print li

    fi = biSearch(li, 7, 0, len(li))
    print fi