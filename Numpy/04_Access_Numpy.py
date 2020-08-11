import numpy as np

def acc_1d():
    print("To access element in 1-D array")
    arr = np.array([1, 2, 3, 4])
    print(arr)
    print("\n")
    print("1st element in the above the array is", arr[0])


def acc_2d():
    print("To access element in 2-D array is")
    arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
    print(arr)
    print("\n")
    print('2nd element on 1st dim in the above the array is: ', arr[0, 1])

def acc_3d():
    print("To access element in 3-D array ")
    arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
    print(arr)
    print("\n")
    print('3rd element on 2nd dim on 1st dim in the above the array is: ',arr[0, 1, 2])

def acc_2d_neg():
    print("To access element in 2-D array using negative index")
    arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
    print(arr)
    print("\n")
    print('Last element from 2nd dim: ', arr[1, -1])


if __name__ == "__main__":
    print("\n")
    acc_1d()
    print("\n")
    acc_2d()
    print("\n")
    acc_3d()
    print("\n")
    acc_2d_neg()
