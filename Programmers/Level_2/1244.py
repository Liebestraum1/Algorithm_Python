n = int(input())
def dfs(num, cnt, depth):
    if cnt == 0:
        answer.append(num)
        return
    if depth == len(num):
        if cnt % 2 == 0:
            answer.append(num)
        elif len(set(num)) != len(num):
            answer.append(num)
        else:
            answer.append(num[:-2] + num[-1] + num[-2])
        return
    for idx in range(depth, len(num)):
        if num[idx] == max(num[depth:]):
            if num[depth] != num[idx]:
                dfs(num[:depth] + num[idx] + num[depth+1:idx] + num[depth] + num[idx+1:], cnt - 1, depth+1)
            else:
                dfs(num, cnt, depth+1)

for case in range(1, n+1):
    data, r = input().split()
    r = int(r)
    answer = []
    dfs(data, r, 0)
    print(f"#{case} {max(answer)}")