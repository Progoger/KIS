import random
import math

rand = random.Random()
n = int(input("Введите кол-во отказов в системе: "))
slices = [rand.randint(0, 5) for i in range(n)]
for i in range(1, len(slices)):
    slices[i] += slices[i-1]
slices = [1, 3, 4, 5, 5, 7, 10, 10, 11, 12, 14, 15, 15, 16, 18]
bound = math.floor(slices[-1]/slices[2])
flag = False
while not flag:
    i = (slices[-1] / bound)
    print(i)
    slices1 = []
    bound -= 1
    tmp = i
    count = 0
    tmp1 = 0
    tmp2 = []
    for j in range(len(slices)):
        if slices[j] > tmp:
            print(slices[j])
            print(len(tmp2))
            tmp += i
            print(tmp)
            if len(tmp2) < 3:
                break
            else:
                slices1.append(tmp2)
            tmp2 = []
            tmp1 = j
        if slices[j] <= tmp:
            tmp2.append(slices[j])
    else:
        slices1.append(tmp2)
        flag = True
        print(slices1)
    print(slices1)

