# Python program to sort a binary array in one pass
 
# Function to put all 0s on left and all 1s on right
def segregate0and1(arr, size):
    # Initialize left and right indexes
    left, right = 0, size-1
    
#    print("left=%d, right=%d" % (left, right))
    while left < right:
        print("Main left=%d, right=%d" % (left, right))
        # Increment left index while we see 0 at left
        while arr[left] == 0 and left < right:
#            print("left=%d, right=%d" % (left, right))
            left += 1
            print("left=%d, right=%d" % (left, right))
 
        # Decrement right index while we see 1 at right
        while arr[right] == 1 and left < right:
#            print("Right left=%d, right=%d" % (left, right))
            right -= 1
            print("Right left=%d, right=%d" % (left, right))
 
        # If left is smaller than right then there is a 1 at left
        # and a 0 at right. Exchange arr[left] and arr[right]
        if left < right:
            arr[left] = 0
            arr[right] = 1
            left += 1
            right -= 1
 
    return arr
 
# driver program to test
# arr = [0, 1, 0, 1, 1, 1]
arr = [1, 0, 0, 1, 1, 1]
arr_size = len(arr)
print("Array after segregation")
print(segregate0and1(arr, arr_size))
 
