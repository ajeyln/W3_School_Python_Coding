import numpy as np

def get_0d():
    print("0-D Array is")
    arr = np.array(42)
    print(arr)

def get_1d():
    print("1-D Array is")
    arr = np.array([1, 2, 3, 4, 5])
    print(arr)

def get_2d():
    print("2-D Array is")
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    print(arr)

def get_3d():
    print("3-D Array is")
    arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
    print(arr)

if __name__ =="__main__":
    get_0d()
    print("\n")
    get_1d()
    print("\n")
    get_2d()
    print("\n")
    get_3d()



