import math

def sun_efficency():
    print("Input the average SUNLIGHT hours (hours): ")
    sunlight_hours = input()
    if sunlight_hours != float():
        return "Error Encountered"
    else:
        y = math.log(sunlight_hours, BASE_HERE)
        ## This is for the log for sunlight hours
        if y >= 10:
            y = 10
        elif y <= 1:
            y = 1
        return y

def wind_efficency():
    print("Input the average wind speed (km/h): ")
    wind_speed = input()
    if wind_speed != float():
        return "Error Encountered"
    else:
        x = 5 * math.log(wind_speed, 9.5)
        if x >= 10:
            x = 10
        elif x <= 1:
            x = 1
        return x

def final_calculations():
    final_wind_effiency = wind_efficency()
    final_sun_effiency = sun_efficency()
    print("Type the amount of money you have available (USD, Millions): ")
    money = input()
    if final_wind_effiency > 5 and final_sun_effiency > 5:
        print("Solar + Wind")
    elif final_sun_effiency > 5:
        print("Solar")
    elif final_wind_effiency > 5:
        print("Wind")
    elif money > INPUT_HERE:
        ## This is for how much money is required to build nuclear
        print("Nuclear")
    else:
        print("No solution available")
    return

print(final_calculations())
