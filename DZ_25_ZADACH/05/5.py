import json

with open("students.json","r",encoding="utf-8") as file:
    students=json.load(file)

for student in students:
    if student["score"]>=60:
        student["passed"]=True
    else:
        student["passed"]=False

best=max(students,key=lambda x:x["score"])

print("Лучший студент:",best["name"])
print("Баллы:",best["score"])

with open("students_result.json","w",encoding="utf-8") as file:
    json.dump(students,file,ensure_ascii=False,indent=4)
