
A=list(input('Enter the password =>'))
B=len(A)
Z=B-1
D=0
b1=int(B/2) 
while b1>0:
    E=A[Z]
    A[Z]=A[D]
    A[D]=E
    D=D+1
    Z=Z-1
    b1=b1-1
AA=''.join(A)
print(AA)
