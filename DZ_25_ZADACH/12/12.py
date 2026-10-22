import re

text="""
Контакты:
alice@example.com
bob@test.org
alice@example.com
admin@company.ru
"""

emails=re.findall(r"[\w.-]+@[\w.-]+\.\w+",text)

emails=list(dict.fromkeys(emails))

for email in emails:
    print(email)
