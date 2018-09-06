import random
data = [random.randint(0, 2000) for i in range(20)]
def bubblesort(data):
    for i in range(len(data) - 1, 1, -1):
        for j in range(0, i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data

print(bubblesort(data))