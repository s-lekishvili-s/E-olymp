N=int(input())
F,L=N//100,N%10
if F>L:
    print(F)
elif F<L:
    print(L)
else:
    print("=")