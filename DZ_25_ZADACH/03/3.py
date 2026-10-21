import csv

scores=[]
groups={}

with open("students.csv","r",encoding="utf-8") as file:
    reader=csv.DictReader(file)

    for row in reader:
        name=row["name"]
        group=row["group"]
        score=int(row["score"])

        scores.append((name,score))

        if group not in groups:
            groups[group]=[]

        groups[group].append(score)

average=sum(score for name,score in scores)/len(scores)

best=max(scores,key=lambda x:x[1])

print("Средний балл:",average)
print("Лучший студент:",best[0])
print("Лучший балл:",best[1])

for group in groups:
    average_group=sum(groups[group])/len(groups[group])
    print("Средний балл группы",group,":",average_group)
