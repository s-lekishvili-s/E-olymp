a , b , c = map (int, input () . split () )
N = (a * b * c)
N1 = N * 6 
s1 = 2 * (a * b + b * c + a * c)
N2 = N1-s1
print (N, N2)