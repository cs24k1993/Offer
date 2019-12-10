import sys
# 4,2,6,4
# 5,3,8,7
# 15
line1 = sys.stdin.readline().strip()
m = list(map(int, line1.split(' ')))
line2 = sys.stdin.readline().strip()
n = list(map(int, line2.split(' ')))
num=m[0]
zuoye=m[1]
cpu=[]
n.sort()
if num>=zuoye:
    print(max(n))
else:
    cpu=n[:num]
    for i in range(num,zuoye):
        cpu[cpu.index(min(cpu))]=cpu[cpu.index(min(cpu))]+n[i]
    print(max(cpu))


