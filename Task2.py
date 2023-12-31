#from collections import deque
from StackQueue import DSAQueue
from main import create_graph


# Function to perform Breadth-First Search (BFS)
def bfs(graph, start_vertex, end_vertex):
    visited = [False] * len(graph)
    parent = [None] * len(graph)
    queue = DSAQueue()
    queue.enqueue(start_vertex)
    visited[start_vertex] = True

    while not queue.isEmpty():
        current_vertex = queue.dequeue()
        if current_vertex == end_vertex:
            break

        for neighbor, _ in graph[current_vertex]:
            if not visited[neighbor]:
                queue.enqueue(neighbor)
                visited[neighbor] = True
                parent[neighbor] = current_vertex

    if parent[end_vertex] is None:
        return None

    path = []
    while end_vertex is not None:
        path.append(end_vertex)
        end_vertex = parent[end_vertex]

    return path[::-1]  # Reverse the path
 # Reverse the path


# Function to perform Depth-First Search (DFS)
def dfs(graph, start_vertex_index):
    visited = [False] * len(graph)
    path = []
    dfs_recursive(graph, start_vertex_index, visited, path)
    return path


def dfs_recursive(graph, current_vertex, visited, path):
    visited[current_vertex] = True
    path.append(current_vertex)
    print("DFS traversal of the graph:", ' -> '.join(chr(current_vertex + ord('A')))) 
    for neighbor, _ in graph[current_vertex]:
        if not visited[neighbor]:
            dfs_recursive(graph, neighbor, visited, path)


def read_uav_data(uav_file):
    uav_data = {}
    with open(uav_file, 'r') as file:
        for line in file:
            values = line.split()
            if len(values) >= 4:
                location = values[0]
                temperature = int(values[1])
                humidity = int(values[2])
                wind_speed = int(values[3])
                uav_data[location] = (temperature, humidity, wind_speed)
    return uav_data



def get_location_data(uav_data, location):
    if location in uav_data:
        temperature, humidity, wind_speed = uav_data[location]
        return (temperature, humidity, wind_speed)
    return None



# Function to display the shortest path and associated data
def display_shortest_path(graph, start_location, end_location, uav_data):
    start_vertex = ord(start_location) - ord('A')
    end_vertex = ord(end_location) - ord('A')
    
    path = bfs(graph, start_vertex, end_vertex)
    if path is None:
        print("No path found.")
        return

    print("Shortest path:", ' -> '.join(chr(vertex + ord('A')) for vertex in path))

    print("Associated data:")
    for vertex in path:
        location = chr(vertex + ord('A'))
        data = get_location_data(uav_data, location)
        if data:
            temperature, humidity, wind_speed = data
            print(f"Location {location}: Temperature={temperature}, Humidity={humidity}, Wind Speed={wind_speed}")
        else:
            print(f"Location {location}: No data available.")

def dfs_traversal(graph,current_node):
    path = dfs(graph,current_node)
    if path is None:
        print("No path found.")
        return

    print("DFS Traversal:", ' -> '.join(chr(vertex + ord('A')) for vertex in path))
    
def main():
    graph = create_graph("location.txt")

    uav_data = read_uav_data("UAVdata.txt")

    # Get user input for start and end locations
    start_location = input("Enter the start location (A-J): ")
    end_location = input("Enter the end location (A-J): ")

    # Display the shortest path and associated data
    display_shortest_path(graph, start_location, end_location, uav_data)
    start_vertex_index = ord(start_location) - ord('A')
    dfs_traversal(graph, start_vertex_index)

if __name__ == '__main__':
    main()
