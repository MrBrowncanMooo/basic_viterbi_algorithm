import time
''' 
    A  B1 B2 B3 C1 C2 C3 D1 D2 D3 E
A   0  6  7  5  0  0  0  0  0  0  0   A B3 C1 D3 E 17
B1  6  0  0  0  5  6  9  0  0  0  0   A B2 C2 D3 E 18
B2  7  0  0  0  4  3  7  0  0  0  0   A B1 C1 D3 E 19
B3  5  0  0  0  4  6  6  0  0  0  0
C1  0  5  4  4  0  0  0  7  8  3  0  
C2  0  6  3  6  0  0  0  5  4  3  0
C3  0  9  7  6  0  0  0  5  7  6  0
D1  0  0  0  0  7  5  5  0  0  0  4
D2  0  0  0  0  8  4  7  0  0  0  8
D3  0  0  0  0  3  3  6  0  0  0  5
E   0  0  0  0  0  0  0  4  8  5  0
'''
# Python3 program to represent directed
# and weighted graph. The program basically
# prints adjacency list representation of graph


weight_index = 1  # weight index
vertex_index = 0  # vertex index

vertex_character = {
    0: 'A',
    1: 'B1',
    2: 'B2',
    3: 'B3',
    4: 'C1',
    5: 'C2',
    6: 'C3',
    7: 'D1',
    8: 'D2',
    9: 'D3',
    10: 'E'

}



# To add an edge
def addEdge(adj, u, v, wt):

    adj[u].append([v, wt])
    return adj


def viterbi_algorithm(adj, stv, endv):
    # list [vertex parent][vertex child] = elements are [vertex '0'+ weight '1']
    virt_list = [[] for _ in range(adj[stv].__len__())]
    for i in range(virt_list.__len__()):
        # adding all vertex conected to starting point
        virt_list[i].append(adj[stv][i])
    short_path_index = []
    small_weight = endv*10

    for i in range(virt_list.__len__()):
        j = 0
        weight = 0
        # you can use the condition of virt_list[i][j] != []:
        while virt_list[i][j][vertex_index] < endv:
            virt_list[i].append(next_vertex(
                adj[virt_list[i][j][vertex_index]]))
            weight += virt_list[i][j][weight_index]
            j += 1
        weight += virt_list[i][j][weight_index]

        if weight < small_weight:
            short_path_index.clear()
            short_path_index = virt_list[i]
            small_weight = weight

    short_path = []
    short_path.append(vertex_character[stv])
    for i in short_path_index:
        short_path.append(vertex_character[i[vertex_index]])
    return short_path


def next_vertex(list_of_node):
    # if not list_of_node:
    #     return list_of_node
    # finding the next vertex by comparing next vertex weight
    min_weight = list_of_node[0]  # intialize the minimum variable
    for i in list_of_node:
        if i[weight_index] < min_weight[weight_index]:
            min_weight = i
    return min_weight


if __name__ == '__main__':

    V = 11
    adj = [[] for i in range(V)]

    adj = addEdge(adj, 0, 1, 6)
    adj = addEdge(adj, 0, 2, 7)
    adj = addEdge(adj, 0, 3, 5)
    adj = addEdge(adj, 1, 4, 5)
    adj = addEdge(adj, 1, 5, 6)
    adj = addEdge(adj, 1, 6, 9)
    adj = addEdge(adj, 2, 4, 4)
    adj = addEdge(adj, 2, 5, 3)
    adj = addEdge(adj, 2, 6, 7)
    adj = addEdge(adj, 3, 4, 4)
    adj = addEdge(adj, 3, 5, 6)
    adj = addEdge(adj, 3, 6, 6)
    adj = addEdge(adj, 4, 7, 7)
    adj = addEdge(adj, 4, 8, 8)
    adj = addEdge(adj, 4, 9, 3)
    adj = addEdge(adj, 5, 7, 5)
    adj = addEdge(adj, 5, 8, 4)
    adj = addEdge(adj, 5, 9, 3)
    adj = addEdge(adj, 6, 7, 5)
    adj = addEdge(adj, 6, 8, 7)
    adj = addEdge(adj, 6, 9, 6)
    adj = addEdge(adj, 7, 10, 4)
    adj = addEdge(adj, 8, 10, 8)
    adj = addEdge(adj, 9, 10, 5)
    start = time.time()
    for _ in range(10):
        print(viterbi_algorithm(adj, 0, 10))
    end1 = time.time()
    print("____%s second____" % (end1-start))
