class Person:
    def __init__(self, name, yob):
        self.name = name
        self. yob = yob
    def describe(self):
        print(f"Name: {self.name} - YoB: {self.yob}")

class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.grade = grade
    def describe(self):
        super().describe()
        print(f"Grade: {self.grade}")

class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.subject = subject
    def describe(self):
        super().describe()
        print(f"Subject: {self.subject}")

class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.specialist = specialist
    def describe(self):
        super().describe()
        print(f"Specialist: {self.specialist}")

class Ward:
    def __init__(self, name):
        self.name = name
        self.ds = []

    #thêm 1 người mới với nghề nghiệp bất kì(student, teacher, doctor)
    def addPerson(self, person):
        for p in self.ds:
            if type(p) == type(person) and p.name == person.name and p.yob == person.yob:
                print("Người này là người cũ.")
                return
        self.ds.append(person)
    
    #đếm số doctor trong ward
    def countDoctor(self):
        d = 0
        for p in self.ds:
            if type(p) == Doctor: #if isinstance(p, Doctor):
                d += 1
        print("Số lượng doctor trong ward: ", d)

    #sort mọi người trong ward theo tuổi của họ với thứ tự tăng dần
    def sortAge(self, reverse=False):
        self.ds.sort(key=lambda p: p.yob, reverse=reverse)
        for p in self.ds:
            p.describe()
    
    #tính trung bình năm sinh của các teacher trong ward
    def aveTeacherYoB(self):
        tong = 0
        d  = 0
        for p in self.ds:
            if type(p) == Teacher:
                d += 1
                tong += p.yob
        if d == 0:
            print("Không có teacher nào trong ward.")
            return
        print("Trung bình yob của các teacher trong ward: ", tong/d)

    #in thông tin ward
    def describe(self):
        print("Ward name: ", self.name)
        for p in self.ds:
            p.describe()

student1 = Student("Linh", 2006, "14")
student1.describe()

teacher1 = Teacher("Châu", 2006, "Cooking")
teacher2 = Teacher("HaHa", 1990, "Laughing")
teacher1.describe()
teacher2.describe()

doctor1 = Doctor("Robin", 2004, "Tai-Mũi-Họng")
doctor2 = Doctor("Round", 2005, "Não")
doctor1.describe()
doctor2.describe()

print()
w1 = Ward("Ward1")
w1.addPerson(student1)
w1.addPerson(teacher1)
w1.addPerson(teacher2)
w1.addPerson(doctor1)
w1.addPerson(doctor2)
w1.describe()
w1.countDoctor()
print("Sắp xếp tuổi theo thứ tự tăng dần:")
w1.sortAge()
w1.aveTeacherYoB()
