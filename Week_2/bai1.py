n = int(input("Nhập n của biểu thức thứ nhất: "))
x = float(input("Nhập x: "))

import math
    
T = 0
for i in range(n+1):
    T += (x**i)/math.factorial(i)
print("Giá trị của e^x là: ", T)

k = int(input("Nhập n của biểu thức thứ hai: "))

S = 0
for e in range(1,k+1):
    S += 1/math.factorial(e)
print("Giá trị biểu thức S là: ", S)