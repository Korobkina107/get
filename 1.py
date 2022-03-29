def right_bin_search(a, b):
    left = 0
    right = len(a)
    while right - left > 1:
        mid = (left + right) // 2
        if a[mid] <= b:
            left = mid
        else:
            right = mid
    if a[left] == b:
        return left
    else:
        return None

def left_bin_search(a, b):
    left = -1
    right = len(a)-1
    while right - left > 1:
        mid = (left + right) // 2
        if a[mid] < b:
            left = mid
        else:
            right = mid
    if a[right] == b:
        return right
    else:
        return None

b=int(input())
a=[-1, -1, 2, 3, 5, 5, 5, 8, 10, 10, 12]
print(right_bin_search(a,b))
print(left_bin_search(a,b))
