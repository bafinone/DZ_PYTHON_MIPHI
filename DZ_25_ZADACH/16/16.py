import re

info=0
warning=0
error=0
error_users=set()

pattern=re.compile(r"\S+\s+\S+\s+(INFO|WARNING|ERROR)\s+User\s+(\d+)")

with open("logs.txt","r",encoding="utf-8") as file:
    for line in file:
        match=pattern.search(line)

        if match:
            level=match.group(1)
            user=match.group(2)

            if level=="INFO":
                info+=1

            elif level=="WARNING":
                warning+=1

            elif level=="ERROR":
                error+=1
                error_users.add(user)

print("INFO:",info)
print("WARNING:",warning)
print("ERROR:",error)
print("Пользователи с ошибками:",error_users)
