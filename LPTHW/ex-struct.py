students = []

for i in range(3):
  name = input("name: ")
  dorm = input("dorm: ")

  student = {"name": name, "dorm": dorm}

  students.append(student)

for student in students:
  print(f"{student['name']} lives in {student['dorm']}")
