graph = {}
vertices = set()


def euler_path(graph, vertices):
    in_degree = dict.fromkeys(vertices, 0)
    out_degree = dict.fromkeys(vertices, 0)

    for vertex in vertices:
        if vertex in graph:
            out_degree[vertex] = len(graph[vertex])
            for adjacent in graph[vertex]:
                in_degree[adjacent] += 1

    start = 0
    for vertex in vertices:
        if in_degree[vertex] < out_degree[vertex]:
            start = vertex

    path, circuit, current = [start], [], start
    while len(path) > 0:
        if out_degree[current]:
            path.append(current)

            out_degree[current] -= 1
            current = graph[current].pop()
        else:
            circuit.append(current)
            current = path.pop()

    circuit.reverse()
    return circuit


with open('out.txt', 'w') as out:
    with open('rosalind_ba3g.txt', 'r') as file:
        for line in file:
            nodes = line.strip().split(' -> ')
            u = int(nodes[0])
            vs = list(map(int, nodes[1].split(',')))

            vertices.add(u)
            vertices |= set(vs)

            graph[u] = vs

    path = euler_path(graph, vertices)
    out.write('->'.join(map(str, path)))
