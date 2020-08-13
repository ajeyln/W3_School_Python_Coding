import numpy as np
def sort_number_np():
    print("Numbers in array to be sorted")
    arr = np.array([3, 2, 0, 1])
    print("Array is")
    print(arr)
    print("Numbers in array after sort")
    print(np.sort(arr))

def sort_alpha_np():
    print(" Element to be sorted aplhbetically")
    arr = np.array(['banana', 'cherry', 'apple'])
    print("Array is")
    print(arr)
    print("Elements in array after sort")
    print(np.sort(arr))

def sort_2d_np():
    print(" Sorting element in 2-D array")
    arr = np.array([[3, 2, 4], [5, 0, 1]])
    print("Array is")
    print(arr)
    print("Elements in 2-D array after sort")
    print(np.sort(arr))

if __name__ == "__main__":
    sort_number_np()
    print("\n")
    sort_alpha_np()
    print("\n")
    sort_2d_np()