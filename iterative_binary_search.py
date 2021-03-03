def search(list1, n):
    l = 0
    u = len(list1) - 1

    while l < u:
        mid = (l + u) // 2
        if list1[mid] == n:
            return True
        else:
            if list1[mid] < n:
                l = mid + 1
            else:
                u = mid - 1
    return False


list1 = [1, 2, 4, 6, 8, 20, 40, 60, 80]

n = 5

if search(list1, n):
    print("number found")
else:
    print("number not found")