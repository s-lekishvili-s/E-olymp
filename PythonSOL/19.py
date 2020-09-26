simmetriya = 0
n = input()
a = len(n)
if(int(a) % 2 == 1):
    simmetriya += 1
for i in range(0, int(a)//2):
    if(n[i] == n[a-(i+1)]):
        simmetriya += 1
print(simmetriya)