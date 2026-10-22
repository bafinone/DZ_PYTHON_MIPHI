def compress(numbers):
    result=[]
    if len(numbers)==0:
        return result
    current=numbers[0]
    count=1
    for i in range(1,len(numbers)):
        if numbers[i]==current:
            count+=1
        else:
            result.append((current,count))
            current=numbers[i]
            count=1
    result.append((current,count))
    return result


def decompress(numbers):
    result=[]
    for value,count in numbers:
        for i in range(count):
            result.append(value)
    return result


numbers=[1,1,1,2,2,5,5,5,5,3]
compressed=compress(numbers)
restored=decompress(compressed)

print("Исходный список:",numbers)
print("Сжатый список:",compressed)
print("Восстановленный список:",restored)
print("Совпадают:",numbers==restored)
