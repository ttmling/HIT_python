import re
email = input("Nhập email: ")
pattern = r'^\w+@\w+\.\w+$'
if re.match(pattern, email):
    print("Valid.")
else:
    print("Invalid.")
