N=int(input())
D=N
while D&D-1:
    D&=D-1
P=M=N
M=(M>>1)+D*(M&1)
while M!=N:
    if M>P:
        P=M
    M=(M>>1)+D*(M&1)
print(P)