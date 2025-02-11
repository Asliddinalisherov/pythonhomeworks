def convert_cel_to_far(cel):
    return round(cel * 9/5 + 32, 2)
def convert_far_to_cel(fah):
    return round((fah-32)*5/9, 2)



# enter in Fahrenheit and display Celsius 
fah = float(input("Enter a temperature in fahrengeit F: "))
cel = convert_far_to_cel(fah)
print(f"{fah} degrees F = {cel} degrees C\n")
# enter in Celsius and display Fahrenheit
cel = float(input("Enter a temperature in degrees C: "))
fah = convert_cel_to_far(cel)
print(f"{cel} degrees C = {fah} degrees F")