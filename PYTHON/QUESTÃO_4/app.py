fator1=2
fator2=3

x=float(input("insira o valor a ser multiplicado: "))

funçao_lambda=lambda x: x*fator1*fator2

resultado=funçao_lambda(x)
print(f"o resultado é {resultado}")