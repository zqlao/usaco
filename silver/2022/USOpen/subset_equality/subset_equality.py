import string
import time
import numpy as np

file_in = '4.in'
f = open(file_in, 'r')
s = f.readline().rstrip()
t = f.readline().rstrip()
# s = input().rstrip()
# t = input().rstrip()
start = time.time()
nums_s = [ord(c) - ord('a') for c in s]
nums_t = [ord(c) - ord('a') for c in t]
cnt_s, cnt_t = [0] * 18, [0] * 18
for i in nums_s:
    cnt_s[i] += 1
for i in nums_t:
    cnt_t[i] += 1
print(f'time {time.time() - start} seconds')

agree = np.ones((18, 18))
for i in range(18):
    x = string.ascii_lowercase[i]
    ind_x_s = [ii for ii, c in enumerate(s) if c == x]
    ind_x_t = [ii for ii, c in enumerate(t) if c == x]
    if len(ind_x_s) != len(ind_x_t):
        for j in range(i):
            agree[i, j] = 0
        continue
    else:
        for j in range(i):
            y = string.ascii_lowercase[j]
            ind_y_s = [ii for ii, c in enumerate(s) if c == y]
            ind_y_t = [ii for ii, c in enumerate(t) if c == y]
            if len(ind_y_s) != len(ind_y_t):
                agree[i, j] = 0
            else:
                sub_s = [s[ind] for ind in sorted(ind_x_s + ind_y_s)]
                sub_t = [t[ind] for ind in sorted(ind_x_t + ind_y_t)]
                if sub_s != sub_t:
                    agree[i, j] = 0
        # agree[i, j] = 1 if sub_s == sub_t else 0
print(f'time {time.time() - start} seconds')
n = int(f.readline().rstrip())

# start = time.time()
rlt = []
for i in range(n):
    # query = input().rstrip()
    query = f.readline().rstrip()
    status = 'Y'
    query_inds = [string.ascii_lowercase.index(c) for c in query]
    if sum([cnt_s[ind] for ind in query_inds]) != sum([cnt_t[ind] for ind in query_inds]):
        status = 'N'
    else:
        for ii, cc in enumerate(query):
            ind_ii = string.ascii_lowercase.index(cc)
            for jj in range(ii):
                ind_jj = string.ascii_lowercase.index(query[jj])
                # if not agree[(cc, query[jj])]:
                if agree[ind_ii, ind_jj]:
                    status = 'N'
                    break
            if status == 'N':
                break
    rlt.append(status)

print(''.join(rlt))
print(f'elapse {time.time() - start} seconds')
