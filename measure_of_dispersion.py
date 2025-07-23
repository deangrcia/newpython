import math

is_running = True
while(is_running):
    try:
        sample = []
        value_minus_mean_squared_total = 0
        for i in range(1, 6):
            try: 
                if i == 1:
                    value_input = int(input(f"Enter {i}st value: "))
                    sample.append(value_input)
                elif i == 2:
                    value_input = int(input(f"Enter {i}nd value: "))
                    sample.append(value_input)
                elif i == 3:
                    value_input = int(input(f"Enter {i}rd value: "))
                    sample.append(value_input)
                elif i == 4 or i == 5:
                    value_input = int(input(f"Enter {i}th value: "))
                    sample.append(value_input)
            except Exception as e:
                sample.clear()
                print("Invalid input. Please try again.")
                break
            
        sample_size = len(sample)
        sample_mean = sum(sample)/sample_size
        sample_range = max(sample) - min(sample)

        for show in sample:
            show -= sample_mean
            value_minus_mean_squared_total += math.pow(show, 2)

        variance = round(value_minus_mean_squared_total/(sample_size-1),2)
        standard_deviation = round(math.sqrt(variance),2)


        print(f"\nRange: {sample_range}\nMean: {sample_mean}\nStandard Deviation: {standard_deviation}\nVariance: {variance}")
        option = input("Continue?").strip.upper
        if option == "Y":
            continue
        else:
            break
    except Exception as e:
        continue