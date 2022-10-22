# file_in = '4.in'
# f = open(file_in, 'r')
# n = int(f.readline().rstrip())
n = int(input().rstrip())
a, v, cnt = [0] * n, [0] * n, [0] * n
for i in range(n):
    # row = f.readline().rstrip().split(' ')
    row = input().rstrip().split()
    a[i], v[i] = int(row[0]) - 1, int(row[1])
    cnt[a[i]] += 1

rlt, circle_cnt, circle_total = sum(v), 0, 0
vis = [0] * n
for i in range(n):
    # find circle in graph - dfs
    if vis[i] == 0:
        p = i
        circle = []
        while vis[p] == 0:
            vis[p] = 1
            circle.append(p)
            p = a[p]
        if a[circle[-1]] in circle:
            while circle[0] != a[circle[-1]]:
                circle.pop(0)
            rlt -= min([v[c] for c in circle])
        # disp('found circle')
print(rlt)
# print(circle_cnt)
# print(circle_total)