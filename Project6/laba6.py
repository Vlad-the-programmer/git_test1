import graf_realization

graph = {
    "v1": ["v2", "v3", "v4", "v7", "v8"],
    "v2": ["v1", "v7", "v8"],
    "v3": ["v1"],
    "v4": ["v1", "v5", "v6"],
    "v5": ["v4", "v6"],
    "v6": ["v4", "v5"],
    "v7": ["v1", "v2", "v8"],
    "v8": ["v1", "v2", "v7"]
}

while 1:
    print("[1] --> DFS (нерекурсивний)")
    print("[2] --> DFS (рекурсивний)")
    print("[3] --> BFS")
    print("[4] --> вийти")
    n = input()


    if n == "1":
            graf_realization.print_dfs_iter(graph, "v1")
            print("\n\n")
    elif  n == "2":
            graf_realization.print_dfs_recur(graph, "v1")
            print("\n\n")
    elif  n == "3":
            graf_realization.print_bfs(graph, "v1")
            print("\n\n")
    elif  n == "4":
            break
