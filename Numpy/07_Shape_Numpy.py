import numpy as np

def disp_shape_np1():
    arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
    print("Orginal 2-D Array is ")
    print(arr)
    print('shape of array :', arr.shape)

def disp_shape_np2():
    arr = np.array([1, 2, 3, 4], ndmin=5)
    print("Orginal 2-D Array is ")
    print(arr)
    print('shape of array :', arr.shape)

if __name__ == "__main__":
    disp_shape_np1()
    print("\n")
    disp_shape_np2()
