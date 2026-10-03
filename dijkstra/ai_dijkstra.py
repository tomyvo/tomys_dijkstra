"""Dijkstra's algorithm: shortest paths from a start node in a weighted graph."""

import heapq


def dijkstra(graph, start):
    """Return (distances, predecessors) for the shortest paths from `start`.

    `graph` maps each node to its neighbors and edge weights:
        {node: {neighbor: weight, ...}, ...}
    """
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    predecessors = {node: None for node in graph}
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Skip stale entries — a shorter path to this node was already found.
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, predecessors


def shortest_path(graph, start, end):
    """Return (distance, path) for the shortest path from `start` to `end`."""
    distances, predecessors = dijkstra(graph, start)
    if distances[end] == float("inf"):
        return float("inf"), []  # no path exists

    path = []
    node = end
    while node is not None:
        path.append(node)
        node = predecessors[node]
    path.reverse()
    return distances[end], path


if __name__ == "__main__":
    graph = {
        "A": {"B": 4, "C": 2},
        "B": {"A": 4, "C": 5, "D": 10},
        "C": {"A": 2, "B": 5, "D": 3},
        "D": {"B": 10, "C": 3, "E": 4},
        "E": {"D": 4},
    }

    start = "A"
    distances, _ = dijkstra(graph, start)
    print(f"Shortest distances from {start}:")
    for node, distance in distances.items():
        print(f"  {start} -> {node}: {distance}")

    print()
    distance, path = shortest_path(graph, "A", "E")
    print(f"Shortest path A -> E: {' -> '.join(path)} (distance {distance})")
