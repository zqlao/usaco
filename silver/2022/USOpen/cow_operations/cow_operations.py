# file_in = '1.in'
# f = open(file_in, 'r')
# s = f.readline().rstrip()
# n = int(f.readline().rstrip())
s = input().rstrip()
n = int(input().rstrip())

cs_c, cs_o, cs_w = [0], [0], [0]
for c in s:
    cs_c.append(cs_c[-1] + (1 if c == 'C' else 0))
    cs_o.append(cs_o[-1] + (1 if c == 'O' else 0))
    cs_w.append(cs_w[-1] + (1 if c == 'W' else 0))

rlt = []
for i in range(n):
    # q = f.readline().rstrip().split()
    q = input().rstrip().split()
    l, r = int(q[0]) - 1, int(q[1])
    cc = (cs_c[r] - cs_c[l]) % 2
    co = (cs_o[r] - cs_o[l]) % 2
    cw = (cs_w[r] - cs_w[l]) % 2

    if co + cw == 1:
        rlt.append('N')
        continue

    if co + cw == 2:
        cc += 1

    if cc == 1:
        rlt.append('Y')
    else:
        rlt.append('N')

print(''.join(rlt))
