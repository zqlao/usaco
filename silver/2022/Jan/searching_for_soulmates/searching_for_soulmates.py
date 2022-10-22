def convert_a(a):
    ans = [a]
    while a > 1:
        if a % 2 == 0:
            a //= 2
        else:
            a += 1
        ans.append(a)
    return ans


def convert_b(b):
    ans = [b]
    while b > 1:
        if b % 2 == 0:
            b //= 2
        else:
            b -= 1
        ans.append(b)
    return ans


def match_a2b(a, b):
    if a == b:
        return 0

    a_sequence = convert_a(a)
    b_sequence = convert_b(b)

    ans = []
    for inda, v in enumerate(a_sequence):
        for d in range(5):
            if v + d in b_sequence:
                indb = b_sequence.index(v + d)
                ans.append(inda + indb + d)

    return min(ans)


n = int(input().rstrip())
pa, pb = [], []
for i in range(n):
    a_, b_ = [int(p) for p in input().rstrip().split(' ')]
    pa.append(a_)
    pb.append(b_)

for i in range(n):
    a_here, b_here = pa[i], pb[i]
    print(match_a2b(a_here, b_here))
