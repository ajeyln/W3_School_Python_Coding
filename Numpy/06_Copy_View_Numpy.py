import numpy as np

def disp_org_np():
    arr = np.array([1, 2, 3, 4, 5])
    print("The Original Array is")
    print(arr)

def disp_copy_np():
    arr = np.array([1, 2, 3, 4, 5])
    x = arr.copy()
    arr[0] = 42
    print("The Original Array After Change")
    print(arr)
    print("The Original Copy array After Change ")
    print(x)

def disp_view_np():
    arr = np.array([1, 2, 3, 4, 5])
    x = arr.view()
    arr[0] = 42
    print("The Original Array After Change")
    print(arr)
    print("The Original View array After Change ")
    print(x)

def chk_data_np():
    arr = np.array([1, 2, 3, 4, 5])
    print("To check copy or view having own data or not")
    print("\n")
    print("The Original Array After Change")
    print(arr)
    x = arr.copy()
    y = arr.view()
    print("Copy array has original data")
    print(x.base)
    print("View array has original data")
    print(y.base)

if __name__ == "__main__":
    arr = np.array([1, 2, 3, 4, 5])
    print(arr)
    disp_org_np()
    print("\n")
    disp_copy_np()
    print("\n")
    disp_view_np()
    print("\n")
    chk_data_np()