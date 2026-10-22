from faker import Faker
import random
fake=Faker("ru_RU")
def generate_file(filename,count):
    with open(filename,"w",encoding="utf-8") as file:
        for i in range(count):
            name=fake.name()
            score=random.randint(0,100)
            file.write(name+";"+str(score)+"\n")

def analyze_file(filename):
    total=0
    count=0
    passed=0
    minimum=None
    maximum=None
    best_student=""
    with open(filename,"r",encoding="utf-8") as file:
        for line_number,line in enumerate(file,start=1):
            line=line.strip()
            if not line:
                continue
            parts=line.rsplit(";",1)
            if len(parts)!=2 or not parts[0].strip():
                print("Некорректная строка:",line_number)
                continue
            name=parts[0].strip()
            try:
                score=int(parts[1])
            except ValueError:
                print("Некорректная оценка в строке:",line_number)
                continue
            total+=score
            count+=1
            if score>=60:
                passed+=1
            if minimum is None or score<minimum:
                minimum=score
            if maximum is None or score>maximum:
                maximum=score
                best_student=name
    if count==0:
        print("Нет корректных записей")
        return
    print("Средний балл:",total/count)
    print("Максимальный балл:",maximum)
    print("Минимальный балл:",minimum)
    print("Набрали не менее 60:",passed)
    print("Лучший студент:",best_student)

generate_file("students.txt",1000)
analyze_file("students.txt")
