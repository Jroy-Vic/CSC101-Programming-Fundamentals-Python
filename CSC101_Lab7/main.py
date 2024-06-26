user_input_tempr = input("Enter a temperature to convert: ")
user_input_scale = input("Enter the scale (C or F) of your temperature: ")

keep_looping = True
while keep_looping == True:
    try:
        tempr_float = float(user_input_tempr)
        keep_looping = False
    except ValueError as e:
        print("An error has occurred:", e)
        print("Please try again.")
        user_input_tempr = input("Enter a temperature to convert: ")

if user_input_scale == "F":
    tempr_c = (tempr_float - 32) * (5/9)
    print("Your temperature in Celsius is", tempr_c)

elif user_input_scale == "C":
    tempr_f = tempr_float * (9/5) + 32
    print("Your temperature in Fahrenheit is", tempr_f)

else:
    print("Sorry, you entered in an unknown scale!")