class Dijkstra:

    def __init__(self, vertices, graph):
        self.vertices = vertices
        self.graph = graph
        print(self.graph)

    def find_route(self, start, end):
        unvisited = {n: float("inf") for n in self.vertices}
        unvisited[start] = 0  # set start vertex to 0
        visited = {}  # list of all visited nodes
        parents = {}  # predecessors
        while unvisited:
            min_vertex = min(unvisited, key=unvisited.get)  # get smallest distance
            for neighbour, _ in self.graph.get(min_vertex, {}).items():
                if neighbour in visited:
                    continue
                # print(unvisited)
                new_distance = unvisited[min_vertex] + self.graph[min_vertex].get(neighbour, float("inf"))
                # print(self.graph[min_vertex])
                if new_distance < unvisited[neighbour]:
                    unvisited[neighbour] = new_distance
                    parents[neighbour] = min_vertex
            visited[min_vertex] = unvisited[min_vertex]
            unvisited.pop(min_vertex)
            if min_vertex == end:
                break
        return parents, visited


    @staticmethod
    def generate_path(parents, start, end):
        path = [end]
        while True:
            key = parents[path[0]]
            path.insert(0, key)
            if key == start:
                break
        return path


input_vertices = ("v0", "v1", "v2", "v3", "v4", "v5", "v6")
input_graph = {
    "v0": {"v2": 5, "v1": 1},
    "v1": {"v0": 1, "v2": 3, "v4": 2, "v6": 20, "v5": 8},
    "v2": {"v0": 5, "v1": 3, "v5": 4},
    "v3": {"v2": 9},
    "v4": {"v1": 2},
    "v5": {"v1": 8, "v2": 4, "v6": 7},
    "v6": {"v1": 20, "v5": 7},

}

while True:

    start_vertex = input("Enter a start vertex: ")
    end_vertex = input("Enter an end vertex: ")
    if start_vertex not in input_vertices or end_vertex not in input_vertices:
        print("One of your vertices s incorrect")
        break
    try:
        dijkstra = Dijkstra(input_vertices, input_graph)
        p, v = dijkstra.find_route(start_vertex, end_vertex)
        print("Distance from %s to %s is: %.2f" % (start_vertex, end_vertex, v[end_vertex]))
        se = dijkstra.generate_path(p, start_vertex, end_vertex)
        print("Path from %s to %s is: %s" % (start_vertex, end_vertex, " -> ".join(se)))
    except KeyError:
        print("There is no path")
