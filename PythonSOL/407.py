T=int(input())
while T:
    T-=1
    N=int(input())
    N%=3
    if N==0:
        print("GCV")
    elif N==1:
        print("VGC")
    else:
        print("CVG")