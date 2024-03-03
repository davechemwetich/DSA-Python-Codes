def print_items(n):
    # Nested for loop is O(n^2)
    for i in range(n):
        for j in range(n):
            print(i,j)
    # This is O(n) for loop
    for k in range(n):
        print(k)
    # result to O(n^2) + O(n) = O(n^2) dorminant term non dominant term dropped
print_items(10)














