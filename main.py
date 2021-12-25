# implementation of Depth Limited First Search Algorithm

# graph representation by using dictionary to act as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': ['J', 'K'],
    'F': ['L', 'M'],
    'G': ['N', 'O'],
    'H': [],
    'I': [],
    'J': [],
    'K': [],
    'L': [],
    'M': [],
    'N': [],
    'O': []

}

# function for dls
def dls(startnode, goal, path, level , maxdepth):
    print('\n This is a Current level: ', level)
    print('Goal node testing for', startnode)
    path.append(startnode)
    if startnode == goal:
        print('Goal test successful')
        return path
    print('Goal node testing failed')
    if level == maxdepth:
        return False
    print('\nExpanding the current node', startnode)
    for child in graph[startnode]:
        if dls(child, goal, path, level + 1, maxdepth):
            return path
        path.pop()
    return False

# Driver Code
startnode = 'A'
goal = input('Enter the goal node:- ')
maxdepth = int(input("Enter the maximum depth limit:-"))
print()
path = list()
res = dls(startnode, goal, path, 0, maxdepth)
if (res):
    print("Path to goal node available")
    print("Path", path)
else:
    print("No path available for the goal node in given depth limit")
