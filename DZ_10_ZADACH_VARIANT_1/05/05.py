import numpy as np
def moving_average(numbers,k):
    if not isinstance(k,int) or k<1 or k>len(numbers):
        raise ValueError("Некорректный размер окна")
    result=[]
    for i in range(len(numbers)-k+1):
        total=0
        for j in range(i,i+k):
            total+=numbers[j]
        result.append(total/k)
    return result


def moving_average_fast(numbers,k):
    if not isinstance(k,int) or k<1 or k>len(numbers):
        raise ValueError("Некорректный размер окна")
    total=sum(numbers[:k])
    result=[total/k]
    for i in range(k,len(numbers)):
        total+=numbers[i]
        total-=numbers[i-k]
        result.append(total/k)
    return result


def moving_average_numpy(numbers,k):
    if not isinstance(k,int) or k<1 or k>len(numbers):
        raise ValueError("Некорректный размер окна")
    result=np.convolve(numbers,np.ones(k)/k,mode="valid")
    return result.tolist()


numbers=[2,4,6,8,10]
k=3

print("Обычный вариант:",moving_average(numbers,k))
print("Быстрый вариант:",moving_average_fast(numbers,k))
print("Вариант NumPy:",moving_average_numpy(numbers,k))
