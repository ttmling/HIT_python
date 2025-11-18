#Tạo mặt hàng (product)
def create_item(name, qty, price):
    data = {}
    data["name"] = name
    data["qty"] = qty
    data["price"] = price
    return data

hoadon = []
hoadon.append(create_item("Pen", 2, 5.0))
hoadon.append(create_item("Notebook", 1, 15.0))
print(hoadon)


#Tính tổng hóa đơn
def calc_total(items):
    total = 0
    for i in items:
        total += i["qty"] * i["price"]
    return total

print(calc_total(hoadon))


#Định dạng hóa đơn thành dạng chuỗi dễ đọc
def format_invoice(customer, items):
    lines = []
    lines.append(f"Customer: {customer}")
    lines.append("-" * 40)
    lines.append(f"{'Product':10} {'Qty':^10} {'Price':^10} {'Subtotal':^10}")
    for product in items:
        lines.append(f"{product["name"]:10} {product["qty"]:^10} {product["price"]:^10.1f} {product["qty"]*product["price"]:^10.1f}")
    lines.append("-" * 40)
    lines.append(f"TOTAL: {calc_total(items):.1f}")
    return "\n".join(lines)

invoice = format_invoice("Nguyen Van A", hoadon)
print(invoice)


#Xuất hóa đơn thành list dòng (dùng để ghi file hoặc hiển thị)
def export_text(invoice_string):
    return invoice_string.split("\n")

lines = export_text(invoice)
print(lines)