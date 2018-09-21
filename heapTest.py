import heapTime
import random

test = {}
heap = heapTime.HeapTime()

for i in range(15):
    test['time'] = random.randint(1,100)
    #print(test)
    heap.add(test)
    #heap.puts()
    #print()
    #print()
while not heap.empty():
    #heap.puts()
    print(heap.pop()['time'])       
#heap.print()
