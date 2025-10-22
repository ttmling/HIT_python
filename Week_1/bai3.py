print("Chao mung den CLB Tin Hoc HIT")

print('CLB Tin Hoc HIT truc thuoc Truong CNTT  - “10 diem”')

s1="CLB Tin Hoc HIT truc thuoc Truong CNTT"
hoa = ' '.join([ch for ch in s1 if ch.isupper()])
thuong = ' '.join([ch for ch in s1 if ch.islower()])
print("cac chu cai in hoa trong chuoi: ", hoa)
print("cac chu cai in thuong trong chuoi: ", thuong)

print(["No", "Yes"]["CNTT" in s1])

s2="CLB Tin Hoc HIT truc thuoc Truong CNTT"
print(s2.swapcase())