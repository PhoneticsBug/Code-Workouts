import sys
input = sys.stdin.readline

n, m = map(int, input().split())
staff = list(map(int, input().split()))

start = 1
end = m*max(staff)

while start <= end:
    mid = (start + end) // 2
    baloon = 0
    for i in staff:
        baloon += (mid // i)
    if baloon < m:
        start = mid + 1
    else:
        end = mid - 1
        result = mid
        
print(result)