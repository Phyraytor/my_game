import random

test = []
for i in range(100):
    test.append(0)
TestCount = 10000
for i in range(TestCount * 100):
    x = random.randint(0, 99)
    test[x] += 1
#for i in range(100):
    #print(i, " = ", round(test[i] / TestCount , 2), "%")
print(round(sum(test[:50]) / TestCount, 3), round(sum(test[50:]) / TestCount, 3) )
