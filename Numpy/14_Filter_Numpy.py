import numpy as np
def filt_bool_np():
    print("Filtering the value in array boolean index method")
    arr = np.array([41, 42, 43, 44])
    print("Array is")
    print(arr)
    print("Boolean index is")
    x = [True, False, True, False]
    newarr = arr[x]
    print("The array after filter boolean index")
    print(newarr)

def filt_val_np():
    print(" Filter the element in array if the value is more than 42")
    arr = np.array([41, 42, 43, 44])
    print("Array is")
    print(arr)
# Create an empty list
    filter_arr = []
# go through each element in arr
    for element in arr:
# if the element is higher than 42, set the value to True, otherwise False:
        if element > 42:
            filter_arr.append(True)
        else:
            filter_arr.append(False)
            
    newarr = arr[filter_arr]
    print("Boolean index is")
    print(filter_arr)
    print("The value in the array, which is more than 42")
    print(newarr)

def filt_even_np():
    print("to find even number in boolean method")
    arr = np.array([1, 2, 3, 4, 5, 6, 7])
# Create an empty list
    filter_arr = []
# go through each element in arr
    for element in arr:
# if the element is completely divisble by 2, set the value to True, otherwise False
        if element % 2 == 0:
            filter_arr.append(True)
        else:
            filter_arr.append(False)
    newarr = arr[filter_arr]
    print("Boolean index is")
    print(filter_arr)
    print("The value in the array, which is more than 42")
    print(newarr)

def filt_val_dir_np():
    print("Filter even number directly from array")
    arr = np.array([41, 42, 43, 44])
    print("Array is")
    print(arr)
    filter_arr = arr > 42
    newarr = arr[filter_arr]
    print("Boolean index is")
    print(filter_arr)
    print("The position of the value in the array, which is more than 42")
    print(newarr)

def filt_even_dir_np():
    print("to find even number directly from Array")
    arr = np.array([1, 2, 3, 4, 5, 6, 7])
    filter_arr = arr % 2 == 0
    newarr = arr[filter_arr]
    print("Boolean index is")
    print(filter_arr)
    print("The position of the even numbers in the array")
    print(newarr)

if __name__ == "__main__":
    filt_bool_np()
    print("\n")
    filt_val_np()
    print("\n")
    filt_even_np()
    print("\n")
    filt_val_dir_np()
    print("\n")
    filt_even_dir_np()