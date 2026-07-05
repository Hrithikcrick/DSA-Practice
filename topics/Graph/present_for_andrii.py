import sys
import heapq

def main():
    data = sys.stdin.read().split()

    if not data:
        return

    n = int(data[0])
    rows = data[1:1 + n]

    mat = []
    parents = [[] for _ in range(n)]
    outdegree = [0] * n
    edges_count = 0

    for i in range(n):
        row = rows[i]
        mat.append(row)

        for j in range(n):
            if row[j] == '1':
                outdegree[i] += 1
                parents[j].append(i)
                edges_count += 1

    heap = []

    for i in range(n):
        if outdegree[i] == 0:
            heapq.heappush(heap, -i)

    topo = [0] * n
    index = n - 1

    while heap:
        node = -heapq.heappop(heap)

        topo[index] = node
        index -= 1

        for par in parents[node]:
            outdegree[par] -= 1

            if outdegree[par] == 0:
                heapq.heappush(heap, -par)

    pos = [0] * n

    for i in range(n):
        pos[topo[i]] = i

    total_possible_edges = n * (n - 1) // 2
    add_count = total_possible_edges - edges_count

    sys.stdout.write(str(add_count) + "\n")

    output = []

    for u in range(n):
        for v in range(n):
            if u == v:
                continue

            if mat[u][v] == '1':
                continue

            if pos[u] < pos[v]:
                output.append(str(u + 1) + " " + str(v + 1) + "\n")

                if len(output) >= 10000:
                    sys.stdout.write("".join(output))
                    output = []

    if output:
        sys.stdout.write("".join(output))

main()
