def calcular_imc (peso, estatura):
    IMC = peso / (estatura *2)
    return IMC
peso = int (input("ingrese su peso en kilogramos: "))
estatura = int (input("ingrese su estatura en metros:"))

imc = calcular_imc (peso, estatura)

print("Tu indice de masa corporal {imc} es:" , imc)