"""

for i in range(1,100 + 1):
    if "5" in str(i) and i % 4 == 0 and i % 5 != 0:
    print("SuperCinco")
    else:
    print(i)
"""
"""
for i in range(1, 500 + 1):
    if ("3" in str (i) or "7" in str(i)) and i % 5 == 0 and i % 10 !=0:
        print("LuckySeven")
    else:
        print(i)
"""
numeros_primos = [2,3,5,7,11,13,17,19]
for i in range (1,500 + 1):
    suma = sum(int(digito) for digito in str(i))
    if "9" not in str(i) and suma in numeros_primos:
        print("PrimeSun")
    else:
        print(i)