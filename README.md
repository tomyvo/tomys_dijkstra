# Dijkstra Shortest Path

A simple Python implementation of **Dijkstra's shortest-path algorithm** using NumPy and Pandas.

The program calculates the shortest path between two nodes in a weighted graph and returns:

* the shortest distance
* the previous node for each visited node
* the shortest path from start to destination
* the total cost/distance of the shortest path

## Features

* Dijkstra's shortest-path algorithm
* Weighted graph support
* Automatic extraction of unique nodes
* Pandas DataFrame for tracking distances and previous nodes
* Detection of unknown start/end nodes
* Detection of unreachable nodes
* Returns the visited-node table, shortest path and total distance

## Requirements

* Python 3.10+
* NumPy
* Pandas

## Installation

Clone the repository and navigate into the project directory:

```bash
git clone <YOUR_REPOSITORY_URL>
cd <PROJECT_DIRECTORY>
```

Create a virtual environment:

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Graph Format

The graph is represented as a list of lists.

Each entry has the following structure:

```python
[start_node, end_node, weight]
```

For example:

```python
nodes = [
    ["AR", "BR", 4],
    ["AR", "CV", 8],
    ["BR", "CV", 2],
    ["BR", "DE", 5],
    ["CV", "DE", 1],
]
```

This represents the following weighted edges:

```text
AR --4--> BR
AR --8--> CV
BR --2--> CV
BR --5--> DE
CV --1--> DE
```

The implementation currently treats the edges as **directed**. Therefore:

```text
AR -> BR
```

does not automatically mean:

```text
BR -> AR
```

## Usage

Import the function and provide the graph, start node and destination node:

```python
from dijkstra import dijkstra

nodes = [
    ["AR", "BR", 4],
    ["AR", "CV", 8],
    ["BR", "CV", 2],
    ["BR", "DE", 5],
    ["CV", "DE", 1],
]

visited_table, path, distance = dijkstra(
    nodes=nodes,
    start="AR",
    end="DE"
)

print(path)
print(distance)
```

Expected shortest path:

```text
['AR', 'BR', 'CV', 'DE']
```

Expected distance:

```text
7
```

## Functions

### `unique_values(card)`

Extracts all unique node names from the graph.

```python
unique_values(nodes)
```

Returns:

```python
['AR', 'BR', 'CV', 'DE']
```

### `table(card)`

Creates a Pandas DataFrame containing all nodes and their current Dijkstra state.

Example:

| node | shortest_distance | previous_node |
| ---- | ----------------- | ------------- |
| AR   | 0                 | nichts        |
| BR   | inf               | nichts        |
| CV   | inf               | nichts        |
| DE   | inf               | nichts        |

### `dijkstra(nodes, start, end)`

Calculates the shortest path between two nodes.

Returns:

```python
visited_table, distance_result, distance
```

Where:

* `visited_table` contains the calculated shortest distances
* `distance_result` contains the shortest path
* `distance` contains the total path cost

## Error Handling

If the start node does not exist:

```text
Diesen Node 'XX' gibt es nicht
```

If the destination node does not exist:

```text
Diesen Node 'XX' gibt es nicht
```

If no path exists:

```text
Kein Weg von AR nach CV vorhanden.
```

## Project Structure

A recommended project structure is:

```text
dijkstra/
│
├── dijkstra.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Running the Program

If the example graph is included in `dijkstra.py`, run:

```bash
python dijkstra.py
```

## Limitations

This is a learning-oriented implementation of Dijkstra's algorithm.

Currently:

* edges are directed
* negative edge weights are not supported
* Pandas is used internally for the algorithm state
* the implementation is not optimized for very large graphs

For large graphs, a priority queue such as Python's `heapq` would generally be more efficient than repeatedly searching a Pandas DataFrame.

## License

This project is available for educational and personal use.
