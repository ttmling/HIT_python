#Tách dữ liệu thành list các tuple (tên, điểm)
n = int(input())
dsach = []
for i in range(n):
    line = input().split()
    ten = line[0]
    diem = [float(x) for x in line[1:]]
    dsach.append((ten, diem))
print(dsach)

#Tạo set chứa các tên duy nhất
set_ten = set()
for a,b in dsach:
    set_ten.add(a)
print(set_ten)

#Với mỗi tên, tính điểm trung bình của sinh viên đó (chỉ dùng list, set, for, if)
ds_dtb = []
for t in set_ten:
    dtb = 0
    for a,b in dsach:
        if t == a:
            dtb = sum(b)/len(b)
    ds_dtb.append((t,dtb))
    print("{} : {}".format(t, dtb))
print(ds_dtb)

#Tìm sinh viên có điểm trung bình cao nhất, thấp nhất
cao_nhat = ds_dtb[0]
thap_nhat = ds_dtb[0]
for sv in ds_dtb[1:]:
    if sv[1] > cao_nhat[1]:
        cao_nhat = sv
    if sv[1] < thap_nhat[1]:
        thap_nhat = sv
print(cao_nhat)
print(thap_nhat)

#Tạo tuple chứa danh sách sắp xếp giảm dần theo điểm trung bình
n = len(ds_dtb)
for i in range(0, n-1):
    for j in range(i+1, n):
        if ds_dtb[i][1] < ds_dtb[j][1]:
            ds_dtb[i], ds_dtb[j] = ds_dtb[j], ds_dtb[i]
print(ds_dtb)