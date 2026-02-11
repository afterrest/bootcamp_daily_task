class max_heap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return max_value

    def _heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] <= self.heap[parent_index]:
                break
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index

    def _heapify_down(self, index):
        size = len(self.heap)
        while True:
            largest = index
            left_child = 2 * index + 1
            right_child = 2 * index + 2

            if left_child < size and self.heap[left_child] > self.heap[largest]:
                largest = left_child

            if right_child < size and self.heap[right_child] > self.heap[largest]:
                largest = right_child

            if largest == index:
                break

            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            index = largest

class min_heap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def extract_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return min_value

    def _heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] >= self.heap[parent_index]:
                break
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index

    def _heapify_down(self, index):
        size = len(self.heap)
        while True:
            smallest = index
            left_child = 2 * index + 1
            right_child = 2 * index + 2

            if left_child < size and self.heap[left_child] < self.heap[smallest]:
                smallest = left_child

            if right_child < size and self.heap[right_child] < self.heap[smallest]:
                smallest = right_child

            if smallest == index:
                break

            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest

class Double_Ended_Priority_Queue:
    def __init__(self):
        self.min_heap = min_heap()
        self.max_heap = max_heap()
        self.entry_count = {}
        self.length = 0

    def insert(self, value):
        self.min_heap.insert(value)
        self.max_heap.insert(value)
        if value in self.entry_count:
            self.entry_count[value] += 1
        else:
            self.entry_count[value] = 1
        self.length += 1

    def delete_min(self):
        while True:
            min_value = self.min_heap.extract_min()
            if min_value is None:
                return None
            if self.entry_count.get(min_value, 0) > 0:
                self.entry_count[min_value] -= 1
                self.length -= 1
                return min_value

    def delete_max(self):
        while True:
            max_value = self.max_heap.extract_max()
            if max_value is None:
                return None
            if self.entry_count.get(max_value, 0) > 0:
                self.entry_count[max_value] -= 1
                self.length -= 1
                return max_value
        

def solution(operations):
    answer = []
    depq = Double_Ended_Priority_Queue()
    for operation in operations:
        if operation == "D 1":
            depq.delete_max()
        elif operation == "D -1":
            depq.delete_min()
        else:
            number = int(operation.split()[1])
            depq.insert(number)
        
    if depq.length == 0:
        answer = [0,0]
    elif depq.length == 1:
        num = depq.delete_max()
        answer = [num, num]
    else:
        ans_max = depq.delete_max()
        ans_min = depq.delete_min()
        answer = [ans_max, ans_min]
            
    return answer

