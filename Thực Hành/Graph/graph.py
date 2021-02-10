#Câu 1
def roadsBuilding(cities, roads):
    rs = []
    arr = [[0 for i in range(cities)] for j in range(cities)]

    for tup in roads:
        source = tup[0]
        dest = tup[1]

        arr[source][dest] = 1
        arr[dest][source] = 1

    for i in range(cities):
        for j in range(cities):
            if i != j and arr[i][j] == 0 and [j, i] not in rs:
                rs.append([i, j])

    return rs
#Câu 3
def greatRenaming(roadRegister):
    l = len(roadRegister)
    arr = [[False for i in range(l)] for j in range(l)]

    for i in range(l):
        a = i - 1
        if i == 0:
            a = l - 1
        for j in range(l):
            b = j - 1
            if 0 == j:
                b = l - 1

            #gan
            arr[i][j] = roadRegister[a][b]

    return arr
#Câu 5
def livingOnTheRoads(roadRegister):
    adj = []
    l = len(roadRegister)

    for i in range(l):
        for j in range(l):
            if roadRegister[i][j] == True and [j, i] not in adj:
                adj.append([i, j])

    adj_len = len(adj)
    arr = [[False for i in range(adj_len)] for j in range(adj_len)]

    for i in range(adj_len):
        for j in range(adj_len):
            if i != j:
                # 0 = [0, 1]
                # 1 = [0, 1]

                dSource = adj[i]
                dDest = adj[j]

                x1 = dSource[0]
                x2 = dSource[1]

                y1 = dDest[0]
                y2 = dDest[1]

                check = False
                if x1 == y1 or x1 == y2 or x2 == y1 or x2 == y2:
                    check = True;

                arr[i][j] = check

    return arr

# if __name__ == '__main__':
#     cities = 4
#     roads = [[0, 1], [1, 2], [2, 0]]
#     print(roadsBuilding(cities, roads))
#
#     roadRegister = [
#         [False, True, True, False],
#         [True, False, True, False],
#         [True, True, False, True],
#         [False, False, True, False]
#     ]
#     print(greatRenaming(roadRegister))
#
#     roadRegister = [
#         [False, True, True, False, False, False],
#         [True, False, False, True, False, False],
#         [True, False, False, False, False, False],
#         [False, True, False, False, False, False],
#         [False, False, False, False, False, True],
#         [False, False, False, False, True, False]
#     ]
#     print(livingOnTheRoads(roadRegister))