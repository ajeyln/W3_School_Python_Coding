import numpy as np

def conv_1d_2d_np():
    print("Covert 1-D to 2-D Array")
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    print("Original 1-D Array is")
    print(arr)
    newarr = arr.reshape(4, 3)
    print("After reshaping the array, Final 2-D Array is")
    print(newarr)

def conv_1d_3d_np():
    print("Covert 1-D to 3-D Array")
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    print("Original 1-D Array is")
    print(arr)
    newarr = arr.reshape(2, 3, 2)
    print("After reshaping the array, Final 3-D Array is")
    print(newarr)

def conv_unknown_known_np():
    print("To convert unknown dimension to known dimension")
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    print("Original Array is")
    print(arr)
    newarr = arr.reshape(2, 2, -1)
    print("3-D Array after reshaping")
    print(newarr)

def conv_muldim_1d_np():
    print("To convert multi dimensional arrays to 1-D Array")
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    print("Original 1-D Array is")
    print(arr)
    print("1-D Array after reshaping is")
    newarr = arr.reshape(-1)
    print(newarr)

def chk_data_np():
    print("To check the reshaped array is Copy or view")
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    print("Original 1-D Array is")
    print(arr)
    print("Array has original data")
    print(arr.reshape(2, 4).base)

if __name__ == "__main__":
    conv_1d_2d_np()
    print("\n")
    conv_1d_3d_np()
    print("\n")
    conv_unknown_known_np()
    print("\n")
    conv_muldim_1d_np()
    print("\n")
    chk_data_np()



