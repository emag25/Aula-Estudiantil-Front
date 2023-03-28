import random


telefonos_existentes = "telefonos_existentes.txt"
with open(telefonos_existentes, "r") as f:
    existing_numbers = [line.strip() for line in f]



generated_numbers = []

while len(generated_numbers) < 50:
    new_number = "09" + str(random.randint(10000000, 99999999))
    if new_number not in existing_numbers and new_number not in generated_numbers:
        generated_numbers.append(new_number)


# Actualizar el archivo de números de exclusión con los números recién generados
with open(telefonos_existentes, "a") as f:
    for num in generated_numbers:
        f.write(num + "\n")


print(len(generated_numbers))
print(', '.join(["'{}'".format(num) for num in generated_numbers]))