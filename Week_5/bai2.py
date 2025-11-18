students = [
    {"id": 1, "name": "An", "score": 8.5},
    {"id": 2, "name": "Bình", "score": 7.2},
    {"id": 3, "name": "Chi", "score": 9.0}
]

#===Câu 1
def find_by_id(data, id):
    for stu in data:
        if stu["id"] == id:
            return stu
    return None

print("Câu 1", find_by_id(students,2))


#===Câu 2
def filter_by_score(data, min_score):
    kq = []
    for stu in data:
        if stu["score"] >= min_score:
            kq.append(stu)
    return kq
#   return list(filter(lambda stu: stu["score"] >= min_score, data))

print("Câu 2", filter_by_score(students, 8.0))


#===Câu 3
def sort_by_score(data, reverse=False):
    return sorted(data, key=lambda stu: stu["score"], reverse=reverse)

print("Câu 3", sort_by_score(students))


#===Câu 4
def add_student(data, student_dict):
    kq = data.copy()
    kq.append(student_dict)
    return kq

new_student = {"id": 4, "name": "Dung", "score": 6.8}
print("Câu 4", add_student(students, new_student))


#===Câu 5
def remove_student(data, id):
    return [stu for stu in data if stu["id"] != id]

print("Câu 5", remove_student(students,2))


#===Câu 6
def statistics(data):
    #điểm trung bình
    tong = 0
    for stu in data:
        tong += stu["score"]
    mean = round(tong/len(data) ,2)

    #dict sinh viên có điểm cao nhất, thấp nhất
    highest = max(data, key=lambda stu: stu["score"])
    lowest = min(data, key=lambda stu: stu["score"])

    #trả về tuple 3 phần tử
    return (mean, highest, lowest)

print("Câu 6", statistics(students))