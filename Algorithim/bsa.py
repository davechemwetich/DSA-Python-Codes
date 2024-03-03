# Test Array
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Target = 5

def binary_search_recursive(arr, target, low, high):
    if high >= low:
        mid = (low + high) // 2  # Find middle point
        
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search_recursive(arr, target, low, mid - 1)
        else:
            return binary_search_recursive(arr, target, mid + 1, high)            
    else:
        return -1  # Target not found

# Test Array
test_array = [2, 3, 4, 10, 40]
target = 10

# Function call
result = binary_search_recursive(test_array, target, 0, len(test_array) - 1)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
