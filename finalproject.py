import math

def sun_efficency():
    print("Input the average SUNLIGHT hours (hours): ")
    sunlight_hours = float(input())
    y = math.log(sunlight_hours, 0.277)
## This is for the log for sunlight hours
    if y >= 10:
        y = 10
    elif y <= 1:
        y = 1
    return y

def wind_efficency():
    print("Input the average wind speed (km/h): ")
    wind_speed = float(input())
    x = 5 * math.log(wind_speed, 9.5)
    if x >= 10:
        x = 10
    elif x <= 1:
        x = 1
    return x

def final_calculations():
    a = sun_efficency()
    b = wind_efficency()
    print("Type the amount of money you have available (USD, Millions): ")
    c = input()
    final_sun_effiency = float(a)
    final_wind_effiency = float(b)
    money = float(c)

    if (final_wind_effiency > 5) and (final_sun_effiency > 5):
        print("Solar + Wind")
    elif final_sun_effiency > 5:
        print("Solar")
    elif final_wind_effiency > 5:
        print("Wind")
    elif money > 1500:
        print("Nuclear")
    else:
        print("No solution available")
    return

final_calculations()
