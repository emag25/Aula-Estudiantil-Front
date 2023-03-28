import random


cedulas_existentes = "cedulas_existentes.txt"
with open(cedulas_existentes, "r") as f:
    excluded_numbers = [line.strip() for line in f]



generated_numbers = set()

while len(generated_numbers) < 50:
    number = ''
    number += str(random.randint(1, 24)).zfill(2)
    number += str(random.randint(0, 5))
    sequential_digits = random.sample(range(10), 6)
    for digit in sequential_digits:
        number += str(digit)
    special_digit = 10 - (int(number) % 10)
    if special_digit == 10:
        special_digit = 0
    number += str(special_digit)
    if number not in excluded_numbers:
        generated_numbers.add(number)



# Actualizar el archivo de números de exclusión con los números recién generados
with open(cedulas_existentes, "a") as f:
    for number in generated_numbers:
        f.write(number + "\n")

print(len(generated_numbers))
print(', '.join(["'{}'".format(num) for num in generated_numbers]))
