"""
    Faca um programa que leia um numero inteiro e mostre na tela o seu sucessor e seu antessesor.
"""

input_num = int( input("Digite um numero ") )

antecessor = input_num - 1
sucessor = input_num + 1

print(f"Analisando o valor {input_num}, seu antecessor e {antecessor} e o sucessor e {sucessor}")

print("Analisando o valor {}, seu antecessor e {} e o sucessor e {}".format(input_num, antecessor, sucessor))

