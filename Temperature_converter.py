# Temperature Converter
# A small program for practising Git and GitHub.
# It converts a temperature from Celsius to Fahrenheit.
#
# How to run it:  python temperature_converter.py

# Ask the user for a temperature in Celsius
celsius = float(input("Temperature in Celsius: "))

# Convert to Fahrenheit
fahrenheit = celsius * 9 / 5 + 32

# Show the result
print("Temperature in Fahrenheit is:", fahrenheit)
kelvin = celsius+273
print("Temperature in kelvin is :", kelvin)  # adding temperature in kelvin
print("Thanks for using it")
