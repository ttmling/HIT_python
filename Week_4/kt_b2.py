tu = input()
duy_nhat = set(tu)
print(duy_nhat)

so_lan = []
for i in duy_nhat:
    lan = tu.lower().count(i)
    so_lan.append(lan)
print(so_lan)

ds = {}