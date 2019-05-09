"""
    Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo pri-
    mitivo e todas as informações possíveis sobre ele.
"""

user_input = input("Digite algo: ")
tipo_primitivo = type(user_input)
length = len(user_input)
is_str = isinstance(user_input, str)
is_int = isinstance(user_input, int)
is_float = isinstance(user_input, float)
is_bool = isinstance(user_input, bool)
is_only_spaces = user_input.isspace()
is_number = user_input.isnumeric()
is_alpha = user_input.isalpha()
is_upper = user_input.isupper()
is_lower = user_input.islower()
is_capitalized = user_input == user_input.capitalize()

print(
    f"""
Tipo primitivo = {tipo_primitivo}
Length = {length}
Is str? = {is_str}
Is int? = {is_int}
Is float? = {is_float}
Is bool? = {is_bool}
Só tem espaços? {is_only_spaces}
É um número? {is_number}
É alphanumérico? {is_alpha}
Esta em maiuscula? {is_upper}
Esta em minuscula? {is_lower}
Esta capitalizada? {is_capitalized}
"""
)
