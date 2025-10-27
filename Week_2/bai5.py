def ktrangay(ngaysinh, thangsinh):
    if thangsinh in [1,3,5,7,8,10,12]:
        return 1 <= ngaysinh <= 31 
    elif thangsinh in [4,6,9,11]:
        return 1 <= ngaysinh <= 30
    elif thangsinh == 2:
        return 1 <= ngaysinh <= 29
    else:
        return False
def chd(ngaysinh, thangsinh):
    if ktrangay(ngaysinh, thangsinh) == False:
        return "invalid"
    match thangsinh:
        case 1:
            return "Ma Kết" if ngaysinh <= 19 else "Bảo Bình"
        case 2:
            return "Bảo Bình" if ngaysinh <= 18 else "Song Ngư"
        case 3:
            return "Song Ngư" if ngaysinh <= 20 else "Bạch Dương"
        case 4:
            return "Bạch Dương" if ngaysinh <= 20 else "Kim Ngưu"
        case 5:
            return "Kim Ngưu" if ngaysinh <= 20 else "Song Tử"
        case 6:
            return "Song Tử" if ngaysinh <= 21 else "Cự Giải"
        case 7:
            return "Cự Giải" if ngaysinh <= 22 else "Sư Tử"
        case 8:
            return "Sư Tử" if ngaysinh <= 22 else "Xử Nữ"
        case 9:
            return "Xử Nữ" if ngaysinh <= 22 else "Thiên Bình"
        case 10:
            return "Thiên Bình" if ngaysinh <= 23 else "Bọ Cạp"
        case 11:
            return "Bọ Cạp" if ngaysinh <= 22 else "Nhân Mã"
        case 12:
            return "Nhân Mã" if ngaysinh <= 21 else "Ma Kết"
        case _:
            return "invalid"

while True:
    ngaysinh = int(input("Nhập vào ngày sinh: "))
    thangsinh = int(input("Nhập vào tháng sinh: "))
    kq = chd(ngaysinh, thangsinh)
    if kq == "invalid":
        print("Ngày hoặc tháng sinh không hợp lệ rồu.")
    else:
        print("Cung hoàng đạo của bạn là: ", kq)
    
    while True:
        nx = input("Bạn có muốn tiếp tục không?(y/n): ").lower()
        if nx == "n":
            print("The end.")
            break
        elif nx == "y":
            break
        else:
            print("Chỉ nhập y/n thôi nha.")
    if nx == "n":
        break

