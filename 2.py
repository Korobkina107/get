def bin_search(a, x):
    left = 0
    right = len(a)
    while right - left > 1:
        mid = (left + right) // 2
        if a[mid] <= x:
            left = mid
        else:
            right = mid
    if a[left] < x:
        return left
    else:
        return None

a=[-1, -1, 2, 3, 5, 5, 5, 8, 10, 10, 12]
b=float(input())
print(bin_search(a, b))