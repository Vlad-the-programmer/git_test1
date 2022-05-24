import copy
class Item():
    previous = None

    def __init__(self, data, next):
        self.data = data
        self.next = next

class Stack():
    data = None
    head = None

    def st_push(self, data):
        temp = Item(data, self.head)
        self.data = data
        self.head = temp

    def st_pop(self):
        if self.head == None:
            print("Стек порожній")
            return
        else:
            a = copy.deepcopy(self.head)
            temp = self.head
            self.head = temp.next

            del temp
            return a.data
    
    def st_show(self):
        temp = self.head

        while temp != None:
            print(temp.data, end=" ")
            temp = temp.next
        
        print()

class Queue():
    rear = None
    front = None

    def enqueue(self, data):
        temp = Item(data, None)
        
        if self.front == None:
            self.front = temp
        else:
            self.rear.next = temp
        
        self.rear = temp
    
    def dequeue(self):
        if self.front == None:
            print("Черга порожня")
            return
        else:
            temp = self.front
            self.front = temp.next
            del temp

    def show(self):
        temp = self.front

        while temp != None:
            print(temp.data, end=" ")
            temp = temp.next
        
        print()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# graph = {
#     "v1": ["v2", "v3", "v4", "v7", "v8"],
#     "v2": ["v1", "v7", "v8"],
#     "v3": ["v1"],
#     "v4": ["v1", "v5", "v6"],
#     "v5": ["v4", "v6"],
#     "v6": ["v4", "v5"],
#     "v7": ["v1", "v2", "v8"],
#     "v8": ["v1", "v2", "v7"]
# }

dfs_dict = {}
def print_dfs_iter(graph, start):

    def dfs_iterable(graph, start):
        visited = [start]
        
        dfs = 1
        dfs_dict[start] = dfs
        
        stack = Stack()
        stack.st_push(start)
        
        frame = []

        print("| Вершина | DFS | Вміст стеку")
        print(f"|   {start}    |  1  | ", end="")
        stack.st_show()

        while stack.head:
            vertex = stack.head.data

            for x in graph[vertex]:
                if x in visited:
                    continue
                
                visited.append(x)

                dfs += 1
                dfs_dict[x] = dfs

                stack.st_push(x)
                frame.append(f"{vertex} - {x}")
        
                print(f"|   {x}    |  {dfs}  | ", end="")
                stack.st_show()
                break
            else:
                print("|    -    |  -  | ", end="")
                stack.st_show()
                stack.st_pop()

        print("\nFrame")
        for x in frame:
            print(x)
        
        dfs_dict.clear()
    
    dfs_iterable(graph, start)


dfs = 0
def print_dfs_recur(graph, vertex):
    res = [vertex]
    visited = []
    frame = []
    print("| Вершина | DFS |")
    
    def dfs_recursive(graph, vertex):
        global dfs

        visited.append(vertex)

        dfs += 1
        dfs_dict[vertex] = dfs
        print(f"|   {vertex}    |  {dfs}  |")

        for x in graph[vertex]:
            if x in visited:
                continue

            res.append(x)
            frame.append(f"{vertex} - {x}")
            dfs_recursive(graph, x)

    dfs_recursive(graph, vertex)

    print("\nFrame")
    for x in frame:
        print(x)



def print_bfs(graph, start):
    bfs_dict = {}

    def bfs(graph, start):
        visited = [start]
        
        bfs = 1
        bfs_dict[start] = bfs

        queue = Queue()
        queue.enqueue(start)

        frame = []

        print("| Вершина | DFS | Вміст черги")
        print(f"|   {start}    |  1  | ", end="")
        queue.show()

        while queue.front:
            vertex = queue.front.data

            for x in graph[vertex]:
                if x in visited:
                    continue
                
                visited.append(x)

                bfs += 1
                bfs_dict[x] = bfs

                queue.enqueue(x)
                frame.append(f"{vertex} - {x}")
        
                print(f"|   {x}    |  {bfs}  | ", end="")
                queue.show()
                break
            else:
                print("|    -    |  -  | ", end="")
                queue.show()
                queue.dequeue()

        print("\nFrame")
        for x in frame:
            print(x)
        
        bfs_dict.clear()

    bfs(graph, start)