import math

while True:
    n = int(input("Nhập vào 1 số nguyên dương: "))
    if n>0:
        break
    else:
        print("Số nguyên dương cơ mà. Nhập lại đi.")

if n <= 2:
    dem = 0
else:
    dem = math.isqrt(n-1) - 1
print("Số các số chính phương(có số ước là lẻ) trong khoảng (1,n) là: ", dem)