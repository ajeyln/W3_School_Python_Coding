import numpy as np
def split_1to3_np():
    print("Split the array into 3 1-D Arrays")
    arr = np.array([1, 2, 3, 4, 5, 6])
    print("Array is")
    print(arr)
    newarr = np.array_split(arr, 3)
    print("Arrays after spliting")
    print(newarr)

def split_1to4_np():
    print("Split the array into 4 1-D Arrays")
    arr = np.array([1, 2, 3, 4, 5, 6])
    print("Array is")
    print(arr)
    newarr = np.array_split(arr, 4)
    print("Arrays after spliting")
    print(newarr)

def split_1to3_row_np():
    print("row wisepliting of an array into 3 parts")
    arr = np.array([1, 2, 3, 4, 5, 6])
    print("Array is")
    print(arr)
    newarr = np.array_split(arr, 3)
    print("Arrays after spliting")
    print(newarr[0])
    print(newarr[1])
    print(newarr[2])

def split_2dto1d_1to3_row_np():
    print("row wise spliting of an 2-d array into 3 1-D arrays")
    arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
    print("Array is")
    print(arr)
    newarr = np.array_split(arr, 3)
    print("Arrays after spliting")
    print(newarr)

def split_2dto2d_1to3_np():
    print("Spliting of an 2-d array into 3 2-D arrays")
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
    print("Array is")
    print(arr)
    newarr = np.array_split(arr, 3)
    print("Arrays after spliting")
    print(newarr)

def split_2dto2d_row_1to3_np():
    print("Row wise spliting of an 2-d array into 3 2-D arrays")
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
    print("Array is")
    print(arr)
    newarr = np.array_split(arr, 3)
    print("Arrays after spliting")
    print(newarr)

def split_2dto2d_stack_1to3_np():
    print("Stack wise spliting of an 2-d array into 3 2-D arrays")
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
    print("Array is")
    print(arr)
    newarr = np.hsplit(arr, 3)
    print("Arrays after spliting")
    print(newarr)

if __name__ == "__main__":
    split_1to3_np()
    print("\n")
    split_1to4_np()
    print("\n")
    split_1to3_row_np()
    print("\n")
    split_1to3_row_np()
    print("\n")
    split_2dto2d_1to3_np()
    print("\n")
    split_2dto2d_row_1to3_np
    print("\n")
    split_2dto2d_stack_1to3_np()