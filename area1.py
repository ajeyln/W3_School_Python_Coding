import math
def get_Area(n):
    return math.pi * n * n

if __name__ == "__main__":
    r = float(input("Enter value of radius:"))
    print(get_Area(r))
