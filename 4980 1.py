# AnthonyLebada
# PART A
# I kept getting 'ValueError: invalid literal for int() with base 10 so this is my workaround...
# and getting decimals was tricky
# Unit Conversion Key (place corresponding letter at end of numerical value)
# "A" = Fahrenheit to Celsius
# "B" = Celsius to Fahrenheit
# "D" = Fahrenheit to Kelvin
# "E" = Celsius to Kelvin
# "G" = Kelvin to Fahrenheit
# "H" = Kelvin to Celsius
Temperature = input("Enter the value you want converted followed by the conversion (Check Unit Conversion Key).")
Unit = int(Temperature[:-1])
typed_unit = Temperature[-1]

if typed_unit.upper() == "A":
    output = int((Unit-32)*5/9)
    returned_unit = "Celsius"
elif typed_unit.upper() == "B":
    output = int((Unit*9)/5+32)
    returned_unit = "Fahrenheit"
elif typed_unit.upper() == "D":
    output = int((((Unit-32)*5)/9)+273)
    returned_unit = "Kelvin"
elif typed_unit.upper() == "E":
    output = int(Unit+273)
    returned_unit = "Kelvin"
elif typed_unit.upper() == "G":
    output = int((((Unit-273)*9)/5)+32)
    returned_unit = "Fahrenheit"
elif typed_unit.upper() == "H":
    output = int(Unit-273)
    returned_unit = "Celsius"
else:
    print("I'm sorry, I did not quite get that. Could you please try again?")
    quit()
print("Your converted temperature is", output, "degrees", returned_unit)

# PART B
Question = input("Enter distance into Conversionatron 3600x PLUS MAX followed by 'i' for inches or 'm' for meters.")
Unit1 = int(Question[:-1])
typed_unit1 = Question[-1]
if typed_unit1.upper() == "I":
    output2 = int(Unit1*0.0254)
    returned_unit1 = "meter(s)"
elif typed_unit1.lower() == "m":
    output2 = int(Unit1*39.3701)
    returned_unit1 = "inch(s)"
else:
    print("That ain't working pal")
    quit()
print("Your converted distance is", output2, returned_unit1)