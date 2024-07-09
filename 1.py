def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 1/8) + 32
    return fahrenheit

def fahrenheit_a_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 1/8
    return celsius

celsius = int(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit_resultado = celsius_a_fahrenheit(celsius)
print(f"{celsius} grados celsius convertidos a {fahrenheit_resultado} grados Fahrenheit")