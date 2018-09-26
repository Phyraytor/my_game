import copy 

class HeapTime:
    def __init__(self) -> None:
        self.heap = []


    def search(self, element: str) -> int:
        for i, items in enumerate(self.heap):
            if items['name'] == element:
                return i
        return -1


    def shiftDown(self, i: int) -> None:
        while 2 * i + 1 < len(self.heap):
            left = 2 * i + 1
            right = 2 * i + 2
            j = left
            if right < len(self.heap) and self.heap[right]['time'] < self.heap[left]['time']:
                j = right
            if self.heap[i]['time'] <= self.heap[j]['time']:
                break
            self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
            i = j


    def shiftUp(self, i: int) -> None:
        while (i - 1) // 2 >= 0 and self.heap[i]['time'] < self.heap[(i - 1) // 2]['time']:
            self.heap[i], self.heap[(i - 1) // 2] = self.heap[(i - 1) // 2], self.heap[i]
            i = (i - 1) // 2


    def pop(self) -> dict:
        if len(self.heap) == 0:
            return {}
        Min = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.shiftDown(0)
        return Min


    def add(self, new_element: dict) -> None:
        self.heap.append( copy.copy(new_element) )
        self.shiftUp( len(self.heap) - 1) 


    def change(self, name:str, stats: dict) -> None:
        i = self.search(name)
        if i < 0: return
        #print("stats = ", stats)
        for k in stats:
            self.heap[i][k] = stats[k]

    '''def insert(self, name:str, stats: dict) -> None:
        i = self.search(name)
        if i < 0: return
        print("stats = ", stats)
        for k in stats:
            self.heap[i][k] = stats[k]'''

    def first(self) -> dict: 
        return self.heap[0] 


    def clear(self) -> None:
        while len(self.heap) > 0:
             self.heap.pop()


    def empty(self) -> bool:
        return len(self.heap) == 0


    def print(self) -> None:
        '''Вывести кучу как массив '''
        for member in self.heap:
            print(member['time'], end = " ")
       # print(self.heap)


    def puts(self) -> None:
        ''' Вывести кучу как пирамиду '''
        i = 1
        if len(self.heap) > 0:
            print(self.heap[0]['time'])  
        while i < len(self.heap):
            for j in range(i, i * 2 + 1):
                if j >= len(self.heap):
                    return
                print(self.heap[j]['time'], end = " ")
            print()
            i = i * 2 + 1

    
    
