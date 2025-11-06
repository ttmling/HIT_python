hang = list(input().split())
print(hang)

duy_nhat = set(hang)
print(duy_nhat)

tpl_duy_nhat = tuple(duy_nhat)
print(tpl_duy_nhat)

so_hang = len(tpl_duy_nhat)
print(so_hang)

ban_chay = {"Phone", "Laptop", "Smartwatch"}
print(duy_nhat.intersection(ban_chay))

print(duy_nhat.difference(ban_chay))

