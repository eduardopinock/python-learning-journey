students = []

students.append("Ana")
students.append("Bela")
students.append("Marta")
students.append("Pina")
students.append("Tete")

students.remove("Marta")

print("REGISTERED STUDENTS")

for name in students:
    print(name)

print("TOTAL OF STUDENTS:", len(students))

new_student = input("WHAT IS YOUR NAME: ")

students.append(new_student)

print("\nUPDATED STUDENT LIST")

for name in students:
    print(name)

print("TOTAL OF STUDENTS:", len(students))