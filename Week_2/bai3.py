while True:
    n = int(input("Nhập vào số lượng học viên: "))
    if n>0:
        break
    else:
        print("Nhập lại đi.")

dsach = []

for hocvien in range(1,n+1):
    print("\nNhập thông tin học viên {}:".format(hocvien))
    hoten = input("Nhập họ tên: ")
    diem1 = int(input("Nhập điểm bài kiểm tra thứ nhất: "))
    diem2 = int(input("Nhập điểm bài kiểm tra thứ hai: "))
    tong = diem1 + diem2
    if tong == 200:
        xeploai = "Xuất sắc"
    elif tong >= 150:
        xeploai = "Giỏi"
    elif tong >= 100:
        xeploai = "Khá"
    else:
        xeploai = "Yếu"
    dsach.append((hocvien, hoten, tong, xeploai))

print("\n=====KẾT QUẢ=====")
for hv in dsach:
    print(hv[0], hv[1], hv[2], hv[3])