import numpy as np
def search_val_ind_np():
    print("To find the position of the value in an array")
    arr = np.array([1, 2, 3, 4, 5, 4, 4])
    print("Array is")
    print(arr)
    x = np.where(arr == 4)
    print("The value 4 is in following positions")
    print(x)

def search_val_ind_even_np():
    print("To find the position of even number in an array")
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    print("Array is")
    print(arr)
    x = np.where(arr%2 == 0)
    print("The even numbers are in following positions")
    print(x)

def search_val_ind_odd_np():
    print("To find the position of odd number in an array")
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    print("Array is")
    print(arr)
    x = np.where(arr%2 == 1)
    print("The odd numbers are in following positions")
    print(x)

def Search_val_sort_np():
    print("To find the position of the value after sorting")
    arr = np.array([6, 7, 8, 9])
    print("Array is")
    print(arr)
    x = np.searchsorted(arr, 7)
    print("The position of the value 7 after sorting")
    print(x)

def search_val_sort_right_np():
    print("To find the position of the value after sorting from right side")
    arr = np.array([6, 7, 8, 9])
    print("Array is")
    print(arr)
    x = np.searchsorted(arr, 7, side='right')
    print("The position of the value 7 after sorting")
    print(x)

def insert_val_sort_np():
    print("In which position the value can be inserted after sorting")
    arr = np.array([1, 3, 5, 7])
    print("Array is")
    print(arr)
    x = np.searchsorted(arr, [2, 4, 9])
    print("The position of these values 2, 4 and 9 can be inserted after sorting")
    print(x)

if __name__ == "__main__":
    search_val_ind_np()
    print("\n")
    search_val_ind_even_np()
    print("\n")
    search_val_ind_odd_np()
    print("\n")
    Search_val_sort_np()
    print("\n")
    search_val_sort_right_np()
    print("\n")
    insert_val_sort_np()