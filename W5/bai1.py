chuoi = input("Nhập chuỗi: ")
stop = ["is", "a"]

#Loại bỏ dấu câu
def remove_punctuation(s):
    s_ko_dau = ""
    for ky_tu in s:
        if ky_tu.isalnum() or ky_tu.isspace():
            s_ko_dau += ky_tu
    return s_ko_dau

print(remove_punctuation(chuoi))


#Chuyển về chữ thường
def to_lower(s):
    return s.lower()

print(to_lower(chuoi))


#Loại bỏ stopwords
def remove_stopwords(s, stop):
    s = s.split()
    for tu in s[:]:
        if tu in stop:
            s.remove(tu)
    return " ".join(s)

print(remove_stopwords(remove_punctuation(chuoi), stop))


#Gộp tất cả
def pipeline(s, functions):
    for ham in functions:
        s = ham(s)
    return s

chuoi_pipeline = pipeline(chuoi, [remove_punctuation, to_lower, lambda x:remove_stopwords(x,stop)])
print(chuoi_pipeline)


#Đếm số lần xuất hiện của từng từ
def count_words(s):
    d = {}
    for tu in s.split():
        if tu not in d:
            d[tu] = 1
        else:
            d[tu] += 1
    return d

print(count_words(chuoi_pipeline))
