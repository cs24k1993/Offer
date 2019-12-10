import sys
# 4,2,6,4
# 5,3,8,7
# 15
line1 = sys.stdin.readline().strip()
m = list(map(int, line1.split(',')))
line2 = sys.stdin.readline().strip()
n = list(map(int, line2.split(',')))
k=int(input())
res = k
m_t = m[:]
n_t = n[:]
for i in range(len(n)):
    if m[i] >= n[i]:
        del m_t[i]
        del n_t[i]
m = m_t[:]
n = n_t[:]
while(len(m)>0):
    m_t = m[:]
    n_t = n[:]
    for i in range(len(m)-1,-1,-1):
        if m[i] < sum:
            sum = sum+n[i]-m[i]
            del m_t[i]
            del n_t[i]
    m=m_t[:]
    n=n_t[:]

print(sum)