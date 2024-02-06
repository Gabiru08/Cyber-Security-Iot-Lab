def primo(numero, divisor=2):
    if numero <= 1:
        return False 
    if divisor * divisor > numero:
        return True  
    if numero % divisor == 0:
        return False  
    return primo(numero, divisor + 1)  


numero = float(input("Insira o numeoro para a verificação: "))
if primo(numero):
    print(f"{numero} é primo.")
else:
    print(f"{numero} não é primo.")
