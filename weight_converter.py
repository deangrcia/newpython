is_running = True
while(is_running):
    try:
        option_input = int(input("\nChoose option [1] Kilogram to Pound [2] Pound to Kilogram\nOption:"))
        if option_input == 1:
            weight_input = float(input("\nEnter Weight(kg): "))
            kilogram_to_pound = round(weight_input * 2.205, 1)
            print(f"Converted to {kilogram_to_pound}lbs")
        elif option_input == 2:
            weight_input = float(input("\nEnter Weight(lbs): "))
            pound_to_kilogram = round(weight_input / 2.205,1)
            print(f"Converted to {pound_to_kilogram}kg")
    except Exception as e:
        print("Invalid input. Please try again.")
        continue