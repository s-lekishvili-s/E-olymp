S=input().split()
k,w=int(S[0]),int(S[1])
S=input().split()
a1,b1,a2,b2,a3,b3=int(S[0]),int(S[1]),int(S[2]),int(S[3]),int(S[4]),int(S[5])
if a1<=w and b1>=k or a2<=w and b2>=k or a3<=w and b3>=k:
    print("YES")
elif a1+a2<=w and b1+b2>=k or a1+a3<=w and b1+b3>=k or a3+a2<=w and b3+b2>=k:
    print("YES")
elif a1+a2+a3<=w and b1+b2+b3>=k:
    print("YES")
else:
    print("NO")