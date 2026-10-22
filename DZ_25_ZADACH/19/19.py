import re

text="""
+7 999 123-45-67
8 999 123-45-67
+7 (999) 123-45-67
8 (999) 123-45-67
"""

pattern=r"(?:\+7|8)\s+(?:\(\d{3}\)|\d{3})\s+\d{3}-\d{2}-\d{2}"

phones=re.findall(pattern,text)

for phone in phones:
    print(phone)
