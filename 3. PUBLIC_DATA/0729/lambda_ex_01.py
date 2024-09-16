students=[('Alice',3.9,20160303),
          ('Bob',3.0,20160302),
          ('Charlie',4.3,20160301)]

sorted_students1=sorted(students,key=lambda s:s[2])
#print(sorted_students1)

sorted_students2=sorted(students,key=lambda s:s[1],reverse=True)
#print(sorted_students2)

#print(sorted(students))

class Student:
    def __init__(self,name,grade,number):
        self.name=name
        self.grade=grade
        self.number=number

    def __repr__(self):
        return f'({self.name}, {self.grade}, {self.number})'

Students=[Student('홍길동',3.9,202403030),
          Student('김유신',3.0,20240302),
          Student('이순신',4.3,20240301)]

print(Students[0])

sorted_list1=sorted(Students,key=lambda s:s.name)
print(sorted_list1)

sorted_list2=sorted(Students,key=lambda s:s.grade)
print(sorted_list2)