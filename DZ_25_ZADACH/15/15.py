def count_lines(stream):
    count=0

    for line in stream:
        count+=1

    return count


with open("data.txt","r",encoding="utf-8") as file:
    print(count_lines(file))
