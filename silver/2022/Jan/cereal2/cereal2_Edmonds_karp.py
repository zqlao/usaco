import copy


def construct_adjacent_edges(nodes_cow, nodes_cereal, pref1lst, pref2lst):
    graph = {}
    for node in nodes_cow + nodes_cereal:
        graph[node] = []
    for ind, v in enumerate(pref1lst):
        graph[nodes_cow[ind]].append((nodes_cereal[v - 1], 1))
    for ind, v in enumerate(pref2lst):
        graph[nodes_cow[ind]].append((nodes_cereal[v - 1], 1))

    # add start node
    graph['start'] = []
    graph['end'] = []

    for node in nodes_cow:
        graph['start'].append((node, 1))
    for node in nodes_cereal:
        graph[node] = [('end', 1)]
    return graph


def construct_graph(cow_num, cereal_num, lst_prefer1, lst_prefer2):
    cow_nodes = []
    for cow_ind in range(1, n + 1):
        cow_nodes.append('cow' + str(cow_ind))
    cereal_nodes = []
    for cereal_ind in range(1, m + 1):
        cereal_nodes.append('cereal' + str(cereal_ind))
    return construct_adjacent_edges(cow_nodes, cereal_nodes, lst_prefer1, lst_prefer2)


def find_path(node_start, node_end, graph2search):
    rlt = [node_start]
    node = node_start
    while node != node_end:
        for node_next in graph2search[node]:
            if not (node_next[0] in rlt):
                rlt.append(node_next[0])
                node = node_next[0]
                break
    return rlt


def find_shortest_path(node_start, node_end, graph2search):
    dist_table = {}
    for node in graph2search:
        dist_table[node] = (False, 10000, 0)  # (visit, min_dist, prev_node)
    q = [node_start]
    dist_table[node_start] = (True, 0, 0)
    while q:
        if dist_table[node_end][0]:
            break
        node = q.pop(0)
        if node == node_end:
            break
        for nn in graph2search[node]:
            if dist_table[nn[0]][0]:
                continue
            q.append(nn[0])
            dist_table[nn[0]] = (True, dist_table[node][1] + 1, node)

    rlt = []
    if dist_table[node_end][0]:
        rlt = [node_end]
        node = node_end
        while node != node_start:
            node = dist_table[node][2]
            rlt.append(node)
        rlt = rlt[::-1]
    return rlt


def is_valid_path(p):
    if ('start' in p) and ('end' in p):
        return True
    else:
        return False


def path_min_weight(p, graph2search):
    weight = []
    for ind_ in range(len(p) - 1):
        node1, node2 = p[ind_], p[ind_ + 1]
        w_ = [nn[1] for nn in graph2search[node1] if nn[0] == node2]
        weight += w_
    return min(weight)


def update_graph(graph2update, path2update):
    min_weight = path_min_weight(path2update, graph2update)
    for ind_ in range(len(path2update) - 1):
        node1, node2 = path2update[ind_], path2update[ind_ + 1]
        node2_ind = [ii for ii, nn in enumerate(graph2update[node1]) if nn[0] == node2][0]
        weight_new = graph2update[node1][node2_ind][1] - min_weight
        if weight_new == 0:
            graph2update[node1].pop(node2_ind)
        else:
            graph2update[node1][node2_ind][1] = weight_new
        graph2update[node2].append((node1, min_weight))
    return graph2update


n, m = [int(c) for c in input().rstrip().split()]

f, s = [], []
for i in range(n):
    f_, s_ = [int(c) for c in input().rstrip().split(' ')]
    f.append(f_)
    s.append(s_)

graph = construct_graph(n, m, f, s)
residual_graph = copy.deepcopy(graph)

rlt = []
while True:
    # path_ = find_path('start', 'end', graph)
    path_ = find_shortest_path('start', 'end', residual_graph)
    if not is_valid_path(path_):
        break
    else:
        cow_ = path_[1][3:]
        if not (cow_ in rlt):
            rlt.append(cow_)
        residual_graph = update_graph(residual_graph, path_)

left = len(residual_graph['start'])
print(str(left))
for r in rlt:
    print(r)
if left > 0:
    for s in residual_graph['start']:
        print(s[0][3:])
# print('done')
