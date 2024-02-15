# 5. Temperature Converter:
# Build a program that converts temperatures between Celsius and Fahrenheit using a dictionary 
# to store conversion factors.
# Temperature in Celsius
dic = {}
temp_celsius = int(input('Enter temperature in Celsius: '))
temp_fahrenheit = temp_celsius + 257
dic[temp_celsius] = temp_fahrenheit
print(f'Temperature in Fahrenheit: {temp_fahrenheit}')
print(dic)
