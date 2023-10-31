weight_kg = float(input("Enter your weight in kilograms:" ))
height_kg = float(input("Enter your height in meters: "))

imc=weight_kg/(height_kg ** 2)

if imc <= 18.5:
    result_imc = "underweight"
elif imc < 25:
    result_imc = "un peso normal"
else:
    result_imc = "owerweight"

print (f"Su imc es :  {imc:.1f}.  Usted tiene  {result_imc}. ")