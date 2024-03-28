def LSearch(x, i, arr):
    print("1. ", x, i, arr)
    if i == len(arr) or x < arr[i]:
        print("B")
        return 0
    if x == arr[i]:
        print("A")
        return 1
    else:
        print("2. ", x, i+1, arr)
        LSearch(x, i+1, arr)

arr = list(map(int, input().split()))
print("Element To Search: ", arr[0])
x = arr[0]
del arr[0]
print("List: ", sorted(arr))
print(LSearch(x, 0, sorted(arr)))
# if LSearch(x, i, sorted(arr)):
#     print("Present")
# else:
#     print("Not Present")
