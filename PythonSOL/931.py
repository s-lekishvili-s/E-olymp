n=input()
H=1
X=0
for i in n:
    H=H*int(i)
    X=X+int(i)
ans=H/X
print("{0:.3f}".format(ans))