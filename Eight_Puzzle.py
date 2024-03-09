from queue import PriorityQueue

# EX :
# start = [
#     [4,1,3],
#     [0,2,6],
#     [7,5,8]
# ]

# end = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,0]
# ]

def h_value(node,end):
    miss=0
    for i in range(len(node)):
        for j in range((len(node))):
            if node[i][j]!=end[i][j] and node[i][j]!=0:
                miss+=1
    return miss

def createNeighbor(node):
    neighbor = []
    row ,col = -1 ,-1
    for i in range(len(node)):
        for j in range((len(node))):
            if node[i][j]==0:
                row , col = i,j
                break
        if row!=-1 and col!=-1:
            break
    # up empty space
    if i>0:
        temp=[row[:] for row in node]
        temp[i][j]=temp[i-1][j]
        temp[i-1][j]=0
        neighbor.append(temp)
    # down empty space
    if i<len(node)-1:
        temp=[row[:] for row in node]
        temp[i][j]=temp[i+1][j]
        temp[i+1][j]=0
        neighbor.append(temp)
    # rigth empty space
    if j<len(node)-1:
        temp=[row[:] for row in node]
        temp[i][j]=temp[i][j+1]
        temp[i][j+1]=0
        neighbor.append(temp)
    # left empty space
    if j>0:
        temp=[row[:] for row in node]
        temp[i][j]=temp[i][j-1]
        temp[i][j-1]=0
        neighbor.append(temp)
    return neighbor

# print(createNeighbor(start))
def a_start_algo(start,end):
    backtrack = {}
    pQueue = PriorityQueue()
    order=0
    g_value={}
    pQueue.put((h_value(start,end),order,start))
    simpleQueue=[start]
    g_value[convert2D(start)]=0
    while not pQueue.empty():
        node=pQueue.get()[2]
        if node==end:
            print("Get : ",node)
            return backtrack
        for neighbor in createNeighbor(node):
            g_value[convert2D(neighbor)] =float('inf')
        for neighbor in createNeighbor(node):
            g_value_temp = g_value[convert2D(node)]+1
            # g_value[convert2D(neighbor)] =float('inf')
            if g_value_temp < g_value[convert2D(neighbor)]:
                g_value[convert2D(neighbor)]=g_value_temp
                h=h_value(neighbor,end)
                backtrack[convert2D(neighbor)]=convert2D(node)
                if neighbor not in simpleQueue:
                    pQueue.put((h,order+1,neighbor))
                    simpleQueue.append(neighbor)
    return False

def makeShortPath(node,backtrack):
    finalPath = []
    while node in backtrack:
        finalPath.append(node)
        node = backtrack[node]
    finalPath.append(convert2D(start))
    finalPath.reverse()
    return finalPath

def convert2D(node):
    node_list = []
    for n in node:
        temp = tuple(n)
        node_list.append(temp)
    return tuple(node_list)

def BFS(start,end):
    backtrack = {}
    visited=[]
    queue=[]
    queue.append(start)
    visited.append(start)

    while queue:
        node=queue.pop(0)
        if node==end:
            print("BFS get",node)
            return backtrack
        node_tuple = convert2D(node)
        for child in createNeighbor(node):
            if child not in visited:
                child_tuple = convert2D(child)
                backtrack[child_tuple]=node_tuple
                queue.append(child)
                visited.append(child)
    return False

if __name__ == "__main__":

    start = []
    end = []

    print("Enter Start Position : ")
    for _ in range(3):
        row = input().strip().split()
        start.append(list(map(int, row)))

    print("Enter End Position : ")
    for _ in range(3):
        row = input().strip().split()
        end.append(list(map(int, row)))

    backtrack=BFS(start,end)
    final_path = makeShortPath(convert2D(end),backtrack)

    print("Short Path : \n")
    for node in final_path:
        for path in node:
            print("\t  ",path)
        print()