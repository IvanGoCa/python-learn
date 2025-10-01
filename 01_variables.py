# Variables
# The variables has to be written in snake case: with '_'.
# WARNING: This is only for python

my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_float_variable = 5.5
print(my_float_variable)

print(my_string_variable, my_int_variable, my_float_variable)

# Funciones del sistema
print(len(my_string_variable))

# Variables en una sola linea
name, surname, edad = "Ivan", "Gomez", 24
print(name, surname, edad)

# Inputs
nameuser = input("Nombre: ")
surname = input("Surname: ")
print(nameuser, surname)

# Forzamos el tipado
address: str = 5
print(type(address))