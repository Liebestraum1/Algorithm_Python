n, m = map(int, input().split())
data = [i for i in range(1, n+1)]
for _ in range(m):
    i, j = map(int, input().split())
    data = data[:i-1] + data[i-1:j][::-1] + data[j:]

print(*data)