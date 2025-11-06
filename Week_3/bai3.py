p = list(input().split())

#Tách tất cả các từ, chuyển hết về chữ thường
thuong = [tu.lower() for tu in p]
print(thuong)

#Tạo một list các từ duy nhất (không trùng), vẫn theo thứ tự xuất hiện
def xoa_trung(ds):
    kq = []
    for phtu in ds:
        if phtu not in kq:
            kq.append(phtu)
    return kq
duy_nhat = xoa_trung(thuong)
print(duy_nhat)

#Đếm số lần xuất hiện của từng từ (bằng cách dùng count() của list hoặc vòng lặp for)
so_lan = []
for tu in duy_nhat:
    lan = thuong.count(tu)
    so_lan.append(lan)
for i in range(len(duy_nhat)):
    print("{}: {}".format(duy_nhat[i], so_lan[i]))

#In ra từ có tần suất xuất hiện cao nhất, từ dài nhất, và tổng số ký tự trong tất cả các từ.
ts_max = so_lan[0]
tu_tsmax = duy_nhat[0]
for i in range(1, len(so_lan)):
    if so_lan[i] > ts_max:
        ts_max = so_lan[i]
        tu_tsmax = duy_nhat[i]
print("{} : {}".format(tu_tsmax, ts_max))

dai_max = duy_nhat[0]
for tu in duy_nhat:
    if len(tu) > len(dai_max):
        dai_max = tu
print(dai_max)

tong_kt = 0
for tu in duy_nhat:
    tong_kt += len(tu)
print(tong_kt)

#In ra danh sách các từ được sắp xếp theo độ dài giảm dần, nhưng không dùng sort()
n = len(duy_nhat)
for i in range(0, n-1):
    for j in range(i+1, n):
        if len(duy_nhat[i]) < len(duy_nhat[j]):
            duy_nhat[i], duy_nhat[j] = duy_nhat[j], duy_nhat[i]
print(duy_nhat)