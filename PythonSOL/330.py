def f(x):
    global G
    if 'A'<=x[0]<='Z':
        x=chr(ord(x[0])+32)+x[1:]
    if G.count(x[-1]):
        x=x[:-1]
    if x==x[::-1]:
        return len(x)
    else:
        return 0
G=",;:.-!?"
m = input().split()
#print(m)
M=P=0
for i in range(len(m)):
    d=f(m[i])
    if d>M:
        P,M=i+1,d
print(P)