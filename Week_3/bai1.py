#Loại bỏ các số trùng lặp nhưng vẫn giữ nguyên thứ tự xuất hiện đầu tiên.
def xoa_trung(ds):
    kq = []
    for phtu in ds:
        if phtu not in kq:
            kq.append(phtu)
    return kq

dsach = list(map(int, input().split()))
dsach_xoa = xoa_trung(dsach)
print(dsach_xoa)

#Tạo danh sách mới: chẵn->bình phương, lẻ->lập phương
dsach_chan = [i*i for i in dsach_xoa if i%2==0]
print(dsach_chan)
dsach_le = [i**3 for i in dsach_xoa if i%2!=0]
print(dsach_le)

#Tính trung bình cộng của các phần tử ở vị trí chỉ số chẵn trong danh sách ban đầu.
def tbc_chan(ds):
    kq = 0
    ds_chan = []
    for i in range(2,len(ds)):
        if i%2 == 0:
            ds_chan.append(ds[i])
    kq = sum(ds_chan)/len(ds_chan)
    return kq
dsach_tbc = tbc_chan(dsach)
print(dsach_tbc)

#Sắp xếp danh sách theo giá trị tuyệt đối tăng dần
def sx(ds):
    for i in range(0, len(ds)-1):
        for j in range(i+1, len(ds)):
            if abs(ds[i]) > abs(ds[j]):
                ds[i],ds[j] = ds[j],ds[i]
    return ds
dsach_sx = sx(dsach_xoa)
print(dsach_sx)
