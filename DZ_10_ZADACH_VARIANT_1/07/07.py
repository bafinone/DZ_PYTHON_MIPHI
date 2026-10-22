import re
import random
from faker import Faker

fake=Faker("ru_RU")
def generate_text(filename,count):
    with open(filename,"w",encoding="utf-8") as file:
        for i in range(count):
            text=fake.name()+" из города "+fake.city()+" любит "
            text+=fake.word()+" и "+fake.word()+"."
            file.write(text+"\n")

def count_words(filename):
    words={}

    with open(filename,"r",encoding="utf-8") as file:
        for line in file:
            line=line.lower()
            line=re.findall(r"[^.,!?:;\s]+",line)
            for word in line:
                if word not in words:
                    words[word]=0

                words[word]+=1
    return words
generate_text("text.txt",10000)
words=count_words("text.txt")
sorted_words=sorted(words.items(),key=lambda x:x[1],reverse=True)
print("10 самых частых слов:")
for word,count in sorted_words[:10]:
    print(word,count)
