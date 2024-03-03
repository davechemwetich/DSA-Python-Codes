def print_items(a,b):
    for i in range(a): # O(a) for loop
        print(i)

    for j in range(b): # O(b) for loop
        print(j)
                       # result to O(a) + O(b) = O(a+b) dorminant term non dominant term dropped
print_items(1, 10)
