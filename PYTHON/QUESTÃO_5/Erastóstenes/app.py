def crivo_eratostenes(n):
   
    primos = [True] * (n + 1)
    primos[0] = primos[1] = False  

    p = 2
    while p * p <= n:
        if primos[p]:
            for i in range(p * p, n + 1, p):
                primos[i] = False
        p += 1

    numeros_primos = [i for i in range(2, n + 1) if primos[i]]
    return numeros_primos


n = int(input("Insira os número até onde deseja a verificação: "))
primos_encontrados = crivo_eratostenes(n)
print("Números primos até", n, "são:", primos_encontrados)
