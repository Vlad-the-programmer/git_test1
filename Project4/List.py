
class Stack:
    def __init__(self, list):
        self.arr = list

    def push(self,  el):
        self.arr.insert(0, el)
        return self.arr

    def show(self):
        if len(self.arr) == 0:
            print("The array is empty! ")
        else:
            print(f"The array is: {self.arr}")

    def pop_the_first_el(self):
        try:
            self.arr.pop(0)
        except IndexError:
            print("The array is empty! ")
        return self.arr

    def __getitem__(self, item):
        return self.arr[self.arr.index(item)]


class LinkedList(Stack):
    def __init__(self, arr, el=None):
        super().__init__(arr)
        self.el = el

    def search(self):
        if self.el in self.arr:
            print("Element Was Found")
        else:
            print("Element Not Found")

    def add_begin(self):

            self.arr.insert(0, self.el)
            return self.arr

    def add_end(self):
        self.arr.append(self.el)
        return self.arr

    def del_begin(self):
        self.arr.pop(0)
        return self.arr

    def del_end(self):
        self.arr.pop()
        return self.arr

    def add_mid(self, el_add, prev_el):
        try:
            self.arr.insert(self.arr.index(prev_el)+1, el_add)
        except ValueError:
            print(f"The el '{prev_el}' is not in the list!")
        return self.arr

    def del_mid(self):
        try:
            self.arr.pop(self.arr.index(self.el))
            return self.arr
        except ValueError:
            print(f"The el  is not in the list!")

    def show(self):
        if len(self.arr) == 0:
            print("The array is empty! ")
        else:
            print(f"The array is: {self.arr}")
        return self.arr

    def exit(self):
        print("Exited")


class Queue:
    def __init__(self, arr,  new_el=None):
        self.new_el = new_el
        self.arr = arr

    def enqueue(self):
        self.arr.append(self.new_el)
        return self.arr

    def dequeue(self):
        try:
            self.arr.pop(0)
        except IndexError:
            print("Queue is empty!")
        return self.arr

    def show(self):
        if len(self.arr) == 0:
            print("The array is empty! ")
        else:
            print(f"The array is: {self.arr}")

    def exit(self):
        print("Exited")







