chuoi = input()

#Loại bỏ các ký tự không phải chữ cái hoặc khoảng trắng
def loai(ds):
    loc = []
    for i in ds:
        if i.isalpha() or i.isspace():
            loc.append(i)
    return loc

chuoi_thuong = "".join(loai(chuoi))
print(chuoi_thuong)

#Chuyển về chữ thường
chuoi_chu_thuong = chuoi_thuong.lower()
print(chuoi_chu_thuong)

#Đếm số nguyên âm và phụ âm trong chuỗi (chỉ tính ký tự chữ)
nguyen_am = "ueoai"
chuoi_chu = "".join(chuoi_chu_thuong.split())
tong_na = 0
tong_pa = 0
tong_na = sum(1 for char in chuoi_chu if char in nguyen_am)
tong_pa = sum(1 for char in chuoi_chu if char not in nguyen_am)
print(tong_na)
print(tong_pa)

#Tách chuỗi thành danh sách từ, sau đó đảo ngược từng từ (không đảo thứ tự các từ)
chuoi_tu = chuoi_thuong.split()
dsach_dao = []
for tu in chuoi_tu:
    dsach_dao.append(tu[::-1])
print(dsach_dao)

#Kiểm tra xem chuỗi có phải là palindrome không (bỏ qua khoảng trắng, hoa/thường).
chuoi_nguoc = chuoi_chu[::-1]
print(chuoi_nguoc == chuoi_chu)