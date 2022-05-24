

# Number of vertices in the graph
V = 6

INF = float('inf')

# Solves all pair shortest path
def printPath(path, v, u, route):
    if path[v][u] == v:
        return
    printPath(path, v, path[v][u], route)
    route.append(path[v][u])

def printsolution(path, n):
    for v in range(n):
        for u in range(n):
            if u != v and path[v][u] != -1:
                route = [v]
                printPath(path, v, u, route)
                route.append(u)
                print(f'The shortest path from {v} —> {u} is', route)

def floydWarshall(graph):

	dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
	path = [[None for x in range(V)] for y in range(V)]

	for v in range(V):
		for u in range(V):
			if v == u:
				path[v][u] = 0
			elif dist[v][u] != float('inf'):
				path[v][u] = v
			else:
				path[v][u] = -1

	for k in range(V):

		# pick all vertices as source one by one
		for i in range(V):

			# Pick all vertices as destination for the
			# above picked source
			for j in range(V):

				# If vertex k is on the shortest path from
				# i to j, then update the value of dist[i][j]
				# if dist[i][j] != INF or dist[i][k] != INF:
				if dist[k][j] != INF and dist[i][k] != INF and (dist[i][k] + dist[k][j] < dist[i][j]):
					dist[i][j] = min(dist[i][j],
								dist[i][k] + dist[k][j]
								)
					path[i][j] = path[k][j]
				if dist[i][i] < 0:
					print('Negative-weight cycle found')
					return
		printSolution(dist)


	printSolution(dist)
	printsolution(path, V)


# A utility function to print the solution
def printSolution(dist):
	print ("Following matrix shows the shortest distances \
between every pair of vertices")
	for i in range(V):
		for j in range(V):
			if(dist[i][j] == INF):
				print ("%7s" % ("INF"),end=" ")
			else:
				print ("%7d" % (dist[i][j]),end=' ')
			if j == V-1:
				print()



graph = [
		[0, 1, 6, INF, INF, INF],
		[INF, 0, 4, INF, -2, INF],
		[INF, INF, 0, INF, 5, 3],
		[2, INF, INF, 0, -5, INF],
		[INF, INF, INF, 8,  0, 4],
		[INF, INF, INF, INF, INF, 0],

]
# graph1 = [
# 		[0, 1, 1, 1, 1, 1],
# 		[2, 0, 2, 2, 2, 2],
# 		[3, 3, 0, 3, 3, 3],
# 		[4, 4, 4, 0, 4, 4],
# 		[5, 5, 5, 5,  0, 5],
# 		[6, 6, 6, 6, 6, 0],
# 		]
#
# # floydWarshall(graph)
floydWarshall(graph)