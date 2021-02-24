import random
import math

rand = random.Random()
n = int(input("Введите кол-во отказов в системе: "))
slices = [rand.randint(0, 5) for i in range(n)]
for i in range(1, len(slices)):
    slices[i] += slices[i-1]
bound = math.floor(slices[-1]/slices[4])
flag = False
while not flag:
    i = (slices[-1] / bound)
    slices1 = []
    bound -= 1
    tmp = i
    count = 0
    tmp1 = 0
    tmp2 = []
    for j in range(len(slices)):
        if slices[j] > tmp:
            tmp += i
            if len(tmp2) < 5:
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
    if len(slices1[-1]) < 5:
        flag = False
for elem in slices1:
    print(elem)
xv = 0
for i in range(len(slices1)):
    xv += len(slices1[i])*slices1[i][0]+slices1[i][-1]/2
xv /= n
lamda = 1/xv
p = []
for i in range(len(slices1)):
    p.append(math.pow(math.e, -lamda*(slices1[i][0]+slices1[i][-1]/2)))
ni = []
for pi in p:
    ni.append(n*pi)
x2 = 0
for i in range(len(slices1)):
    x2 += math.pow(len(slices1[i]) - ni[i], 2) / ni[i]
print("Наше: ", x2)
r = len(slices1) - 2
xp = -2.33
x2_tabl = r + 2*math.sqrt(2*r)*xp + 2/3*math.pow(xp, 2) - 2/3 + 1/math.sqrt(r)
print("Табличное: ", x2_tabl)
if x2 >= x2_tabl:
    print("гипотеза подтверждается")
else:
    print("гипотеза опровергается")