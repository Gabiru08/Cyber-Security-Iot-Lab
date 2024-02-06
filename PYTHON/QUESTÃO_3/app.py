def soma(multiplicador=1, *valores):
    resultado=sum(valores)
    resultado_multiplicado = resultado * multiplicador 
    return resultado, resultado_multiplicado

entrada= input("Insira os valores para a soma: ")
valores = [float(valor) for valor in entrada.split()]


multiplicador = float(input("Insira o multiplicador: "))

resultado_soma, resultado_soma_multiplicada = soma (multiplicador, *valores)


print(f"O valor da soma é {resultado_soma}")
print(f"O valor da soma multiplicada por {multiplicador} é {resultado_soma_multiplicada}")
