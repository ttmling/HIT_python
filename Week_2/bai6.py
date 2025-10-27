menu = []
tongtien = 0
while True:
    mon = input("Nhập tên món: ")
    if mon.lower() == "x":
        break
    elif mon.lower() == "skip":
        continue
    elif mon.lower() == "pass":
        gia = 0
        pass
    else:
        gia = int(input("Nhập giá của món: "))
    menu.append((mon, gia))
    tongtien += gia

soMon = 0
for mon in menu:
    soMon += 1

giamgia = 0
if tongtien > 200000:
    giamgia = tongtien*0.1
    tong = tongtien*0.9
else:
    giamgia = 0
    tong = tongtien

print("\n=====HÓA ĐƠN=====")
print("Số món: ", soMon)
print("Tổng tiền trước giảm: ", tongtien)
print("Giảm giá: ", giamgia)
print("Tổng tiền phải trả: ", tong)