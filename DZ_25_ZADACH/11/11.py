import re

with open("logs.txt","r",encoding="utf-8") as file:
    text=file.read()
users=re.findall(r"User (\d+)",text)
errors=[]
for line in text.splitlines():
    if "ERROR" in line:
        errors.append(line)
error_users=re.findall(r"ERROR User (\d+)",text)
print("Все пользователи:",users)
print("Ошибки:")
for line in errors:
    print(line)
print("Пользователи с ошибками:",set(error_users))
