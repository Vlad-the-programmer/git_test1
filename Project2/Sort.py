

class Sort():

    def __init__(self, list):
        self.list = list

    def _swap(self, x, y):
        temp = self.list[x]
        self.list[x] = self.list[y]
        self.list[y] = temp


    def SortBubble(self):
        index_of_last_el = len(self.list) - 1
        while True:
            for run in range(index_of_last_el, 0, -1):
                for iter in range(run):
                    if self.list[iter] > self.list[iter + 1]:
                        self._swap(
                        iter,iter + 1)
            return self.list

    def show(self):
        return self.list


    def SortInsertion(self):
        indexing_length = range(1, len(self.list))

        for i in indexing_length:
            value_to_sort = self.list[i]

            while self.list[i-1] > value_to_sort and i > 0:
                
                self._swap(i,i-1)
                i -= 1
        return self.list

    def MinItem(self, start, end):
        min_value = start
        for i in range(start, end):
            if self.list[i] < self.list[min_value]:
                min_value = i
        return min_value

    def SortSelection(self):
        indexing_length = range(0, len(self.list)-1)

        for i in indexing_length:
            min_value = i
            for j in range(i+1, len(self.list)):
                if self.list[j] < self.list[min_value]:
                    min_value = j

            if min_value != i:
                self._swap(min_value,i)

        return self.list
    
    def show(self):
        return self.list


#in-place sorting

class Modified_Sort(Sort):
  
    def __init__(self, list, sorting_from, sorting_to):
        super().__init__(list)
        self.sorting_from = int(sorting_from)
        self.sorting_to = int(sorting_to)

    # def __str__(self):
    #     self.list

    def SortBubble(self):
  
        while True:
            for run in range(self.sorting_from, self.sorting_to):
                for iter in range(self.sorting_to-1, run, -1):
                    if self.list[iter-1] > self.list[iter]:
                
                        self._swap(
                        iter-1, iter)

            # print(self.list)
            return self.list
    
    def SortInsertion(self):
        indexing_length = range(self.sorting_from, self.sorting_to)

        for i in indexing_length:
            value_to_sort = self.list[i]

            while self.list[i-1] > value_to_sort and i > 0:
                
                self._swap(i, i-1)

                i -= 1
        return self.list
    
    def SortSelection(self):
        indexing_length = range(self.sorting_from, self.sorting_to)

        for i in indexing_length:
            min_value = i
            for j in range(i+1, self.sorting_to):
                if self.list[j] < self.list[min_value]:
                    min_value = j 

            if min_value != i:
                self._swap(min_value,i)

        return self.list

    def _show(self):
          super().show()
