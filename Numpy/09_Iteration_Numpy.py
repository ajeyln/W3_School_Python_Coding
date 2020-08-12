import numpy as np
def iter_1d_np():
    print("Iteration of 1-D Array")
    arr = np.array([1, 2, 3])
    print("Original 1-D Array is")
    print(arr)
    print("\n")
    for x in arr:
        print("The Element after iteration")
        print(x)

def iter_2d_np():
    print("Iteration of 2-D Array")
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    print("Original 2-D Array is")
    print(arr)
    print("\n")
    for x in arr:
        print("The element after 1st time iteration in 2-D Array")
        print(x)
        for y in x:
            print("The element after 2nd time iteration in 2-D Array")
            print(y)

def iter_3d_np():
    print("Iteration of 3-D Array")
    arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
    print("Original 2-D Array is")
    print(arr)
    print("\n")
    for x in arr:
          print("The element after 1st time iteration in 3-D Array")
          print(x)
          for y in x:
              print("The element after 2nd time iteration in 3-D Array")
              print(y)
              for z in y:
                  print("The element after 3rd time iteration in 3-D Array")
                  print(z)

def iter_3d_np2():
    print("Iteration of 3-D Array using nditer")
    arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
    print("Original 3-D Array is")
    print(arr)
    print("\n")
    for x in np.nditer(arr):
        print("The element after nditer in 3-D Array")
        print(x)

def conv_datatype_np():
    arr = np.array([1, 2, 3])
    print("Original 3-D Array is")
    print(arr)
    print("\n")
    for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
        print("The element after changing the datatype")
        print(x)

def iter_custom_np():
    print("To iterate Alternative element in 2-D")
    arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
    print("Original 2-D Array is")
    print(arr)
    print("\n")
    for x in np.nditer(arr[:, ::2]):
        print("The element after iteration by steps method")
        print(x)

def iter_index_1d_np():
    print("Iterating with Index and dimension in 1-D Array")
    arr = np.array([1, 2, 3])
    print("Original 1-D Array is")
    print(arr)
    print("\n")
    for idx, x in np.ndenumerate(arr):
        print("The final value is")
        print(idx, x)

def iter_index_2d_np():
    print("Iterating with Index and dimension in 2-D Array")
    arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
    print("Original 1-D Array is")
    print(arr)
    print("\n")
    for idx, x in np.ndenumerate(arr):
        print("The final value is")
        print(idx, x)

if __name__ == "__main__":
    iter_1d_np()
    print("********************************************************")
    print("\n")
    iter_2d_np()
    print("********************************************************")
    print("\n")
    iter_3d_np()
    print("********************************************************")
    print("\n")
    iter_3d_np2()
    print("********************************************************")
    print("\n")
    conv_datatype_np()
    print("********************************************************")
    print("\n")
    iter_custom_np()
    print("********************************************************")
    print("\n")
    iter_index_1d_np()
    print("********************************************************")
    print("\n")
    iter_index_2d_np()









