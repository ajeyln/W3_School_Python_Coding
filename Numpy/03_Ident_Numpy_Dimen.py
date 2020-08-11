import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(a)
print("The dimension of the above array is:",+ a.ndim)
print("\n")
print(b)
print("The dimension of the above array is:",+ b.ndim)
print("\n")
print(c)
print("The dimension of the above array is:",+ c.ndim)
print("\n")
print(d)
print("The dimension of the above array is:",+ d.ndim)
print("\n")