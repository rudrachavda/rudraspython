airports = ["BGI", "CDG", "DEL", "DOH", "DSM", "EWR", "EYW", "HND", "ICN" "JFK", "LGA", "LHR", "ORD", "SAN", "SFO", "SIN", "TLV", "BUD", ]

#one way flight
routes = [ 
["ORD", "BGI"],
["BGI", "LGA"],
["SIN", "CDG"],
["CDG", "SIN"],
["CDG", "BUD"],
["DEL", "DOH"],
["DEL", "CDG"],
["TLV", "DEL"],
["EWR", "HND"],
["HND", "ICN"],
["HND", "JFK"],
["ICN", "JFK"],
["JFK", "LGA"],
["EYW", "LHR"],
["LHR", "SFO"],
["SFO", "SAN"],
["SFO", "DSM"],
["SAN", "EYW"],
]

startingAirport = "LGA"

import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

# Build a graph representation from the routes array
graph = defaultdict(list)
for route in routes:
    src, dest = route
    graph[src].append(dest)
    graph[dest].append(src)  # Add the backward route as well

# Function to perform Depth-First Search (DFS) in the graph
def dfs(node, visited, stack):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, visited, stack)
    stack.append(node)

# Function to perform Reverse Depth-First Search (DFS) in the graph
def reverse_dfs(node, visited, component):
    visited.add(node)
    component.append(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            reverse_dfs(neighbor, visited, component)

# Kosaraju's algorithm to find the strongly connected components and shortest route
def find_shortest_route(start, end):
    visited = set()
    stack = []
    components = []
    for airport in airports:
        if airport not in visited:
            dfs(airport, visited, stack)

    visited.clear()
    shortest_route = []
    while stack:
        node = stack.pop()
        if node not in visited:
            component = []
            reverse_dfs(node, visited, component)
            components.append(component)
            if start in component and end in component:
                start_component = next(c for c in components if start in c)
                end_component = next(c for c in components if end in c)
                if start_component == end_component:
                    start_index = component.index(start)
                    end_index = component.index(end)
                    if start_index < end_index:
                        shortest_route = component[start_index:end_index + 1]
                    else:
                        shortest_route = component[end_index:start_index + 1][::-1]
                    break

    return shortest_route

# Find the shortest route from LGA to the user-specified destination
print("Starting airport: " + startingAirport)
print("Available airports: " + str(airports))
endingAirport = input("Enter Destination: ")

shortest_route = find_shortest_route(startingAirport, endingAirport)
if shortest_route:
    print("Shortest route: " + str(shortest_route))
else:
    print("No valid route found.")

# Create a graph visualization
G = nx.Graph()
G.add_nodes_from(airports)

# Set the color of the airports in the shortest route to a different color
node_colors = ['lightblue' if airport in shortest_route else 'lightgray' for airport in airports]

# Draw the graph
pos = nx.spring_layout(G, seed=42)
nx.draw_networkx(G, pos, node_color=node_colors, with_labels=True)
plt.title("Airport Routes")
plt.show()
