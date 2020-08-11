import numpy as np

def slic_1d():
    print("To print some slice/part of the element in 1-D array")
    arr = np.array([1, 2, 3, 4, 5, 6, 7])
    print(arr)
    print("\n")
    print("The elements from 2nd to till 5th in the above array are: ")
    print(arr[1:5])
    print("\n")
    print("The elements from 2nd to 4th element with slicing 2 indexes in the above array are:")
    print(arr[1:5:2])
    print("\n")
    print("The every alternative elements in the above array are:")
    print(arr[::2])
    print("\n")
    print("The elements from 5th to till end in the above array are: ")
    print(arr[4:])
    print("\n")
    print("The elements from beggining to till 4th in the above array are: ")
    print(arr[:4])
    print("\n")

def slic_1d_neg():
    print("To print some slice/part of the element in 1-D array using negative indexing")
    arr = np.array([1, 2, 3, 4, 5, 6, 7])
    print(arr)
    print("\n")
    print("The element from 3rd to 1st element from end of the above array is ")
    print(arr[-3:-1])

def slic_2d():
    print("To print some slice/part in 2-D array")
    arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
    print(arr)
    print("\n")
    print("The elements from 2nd to 4th from 2nd array in 2nd dem:")
    print(arr[1, 1:4]) 
    print("\n")
    print("The 3rd element from each array in 2nd dem:")
    print(arr[0:2, 2])
    print("\n")
    print("The elements from 2nd to 4th from 1st and 2nd array in 2nd dem:")
    print(arr[0:2, 1:4])

if __name__ == "__main__":
    print("\n")
    slic_1d()
    print("\n")
    slic_1d_neg()
    print("\n")
    slic_2d()
  
