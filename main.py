class Vertex:
    def __init__(self, ID, kind):
        self.ID = ID
        self.kind = kind
        self.adjacent = {}

    def __str__(self):
        return str(self.ID) + ' adjacent: ' + str([x.ID for x in self.adjacent])

    def add_neighbor(self, neighbor, weight):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.ID

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]


class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, ID, kind):
        if ID not in self.vert_dict:
            self.num_vertices = self.num_vertices + 1
            new_vertex = Vertex(ID, kind)
            self.vert_dict[ID] = new_vertex
            # return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost):
        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        # self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()


g = Graph()

R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))

# Initialize matrix
matrix = []
# For user input
for i in range(R):  # A for loop for row entries
    a = []
    for j in range(C):  # A for loop for column entries
        a.append(input())
    matrix.append(a)


def coords(i, j, R, C):
    def up():
        if j - 1 > 0:
            dest = matrix[i][j - 1]
            cost = 0
            if not dest.__contains__('x'):
                if dest.__contains__('b') or dest.__contains__('p'):
                    cost = int(dest.replace(dest[len(dest) - 1], ''))
                    g.add_vertex(i + C * j, dest[len(dest) - 1])
                else:
                    cost = int(dest)
                    g.add_vertex(i + C * j, 'none')
                g.add_edge(i + C * j, i + C * j - 1, cost)
                coords(i, j - 1, R, C)

    def down():
        if j + 1 < R:
            dest = matrix[i][j + 1]
            cost = 0
            if not dest.__contains__('x'):
                if dest.__contains__('b') or dest.__contains__('p'):
                    cost = int(dest.replace(dest[len(dest) - 1], ''))
                    g.add_vertex(i + C * j, dest[len(dest) - 1])
                else:
                    cost = int(dest)
                    g.add_vertex(i + C * j, 'none')
                g.add_edge(i + C * j, i + C * j + 1, cost)
                coords(i, j + 1, R, C)

    def right():
        if i + 1 < C:
            dest = matrix[i + 1][j]
            cost = 0
            if not dest.__contains__('x'):
                if dest.__contains__('b') or dest.__contains__('p'):
                    cost = int(dest.replace(dest[len(dest) - 1], ''))
                    g.add_vertex(i + C * j, dest[len(dest) - 1])
                else:
                    cost = int(dest)
                    g.add_vertex(i + C * j, 'none')
                g.add_edge(i + C * j, i + C * j - 1, cost)
                coords(i + 1, j, R, C)

    def left():
        if i - 1 > 0:
            dest = matrix[i - 1][j]
            cost = 0
            if (not dest.__contains__('x')):
                cost = int(dest.replace(dest[len(dest) - 1], ''))
                if dest.__contains__('b') or dest.__contains__('p'):
                    g.add_vertex(i + C * j, dest[len(dest) - 1])
                else:
                    cost = int(dest)
                    g.add_vertex(i + C * j, 'none')
                g.add_edge(i + C * j, i + C * j - 1, cost)
                coords(i - 1, j, R, C)

    up()
    down()
    right()
    left()


flag = True

Robot_i = 0
Robot_j = 0
for i in range(R):
    if flag:
        for j in range(C):
            if matrix[i][j].__contains__('r'):
                Robot_i = i
                Robot_j = j
                flag = False
                break

coords(Robot_i, Robot_j, R, C)