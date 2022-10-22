n = int(input().rstrip())
h = [int(i) for i in input().rstrip().split(' ')]


# def dfs(hh):
#     ans = 0
#     seg_stack = [[0, len(hh)]]
#     while seg_stack:
#         seg = seg_stack.pop(0)
#         hh_ = hh[seg[0]:seg[1]]
#         if len(hh_) < 2:
#             continue
#         elif len(hh_) == 2:
#             ans += 2
#             continue
#         else:
#             nn = len(hh_)
#             ind = hh_.index(max(hh_))
#             if ind == 0:
#                 delta, v_max = 0, 0
#                 for i, v in enumerate(hh_[1:]):
#                     if v > v_max:
#                         v_max = v
#                         delta += i + 2
#                 ans += delta
#                 seg_stack.append([seg[0]+1, seg[1]])
#                 # return dfs(hh[1:]) + delta
#             elif ind == nn - 1:
#                 delta, v_max, hh_here = 0, 0, hh_[:-1]
#                 for i in range(len(hh_here) - 1, -1, -1):
#                     if hh_here[i] > v_max:
#                         v_max = hh_here[i]
#                         delta += ind - i + 1
#                 ans += delta
#                 seg_stack.append([seg[0], seg[1]-1])
#                 # return dfs(hh[:-1]) + delta
#             else:
#                 hh_left, hh_right = hh_[:ind], hh_[ind + 1:]
#                 delta, v_max = 0, 0
#                 for i in range(len(hh_left) - 1, -1, -1):
#                     if hh_left[i] > v_max:
#                         v_max = hh_left[i]
#                         delta += ind - i + 1
#                 seg_stack.append([seg[0], seg[0]+ind])
#                 v_max = 0
#                 for i, v in enumerate(hh_right):
#                     if v > v_max:
#                         v_max = v
#                         delta += i + 2
#                 ans += delta
#                 seg_stack.append([seg[0]+ind+1, seg[1]])
#                 # return dfs(hh[:ind]) + dfs(hh[ind + 1:]) + delta
#     return ans

def dfs(hh):
    ans, nn = 0, len(hh)
    stk = []
    for i in range(nn - 1, -1, -1):
        while stk and hh[i] > hh[stk[-1]]:
            stk.pop()
        if stk:
            ans += stk[-1] - i + 1
        stk.append(i)
    return ans


print(dfs(h) + dfs(h[::-1]))
