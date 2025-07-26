def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return f"{celsius}C = {fahrenheit}F"

def fahrenheit_to_kelvin(fahrenheit):
    kelvin = (fahrenheit - 32) * 5/9 + 273.15
    return f"{fahrenheit}F = {kelvin}K"

def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return f"{kelvin}K = {celsius}C"
    
"""Demonstation of all functions one by one"""

print(celsius_to_fahrenheit(0))
print(fahrenheit_to_kelvin(32))
print(kelvin_to_celsius(273.15)) 
