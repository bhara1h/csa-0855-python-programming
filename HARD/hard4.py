def get_season(month, day):
    if (month == "Mar" and day >= 20) or (month in ["Apr", "May"]) or (month == "Jun" and day < 21):
        return "Summer"
    elif (month == "Jun" and day >= 21) or (month in ["Jul", "Aug"]) or (month == "Sep" and day < 22):
        return "Spring"
    elif (month == "Sep" and day >= 22) or (month in ["Oct", "Nov"]) or (month == "Dec" and day < 21):
        return "Fall"
    else:
        return "Winter"

# Read input from the user
month = input("Enter the month (First three letters, capitalized): ")
day = int(input("Enter the day: "))

# Determine and display the season
season = get_season(month, day)
print(f"The season is currently {season}.")

# Test Cases
print(f"{get_season('Jul', 29)}")  # Expected Output: Spring
print(f"{get_season('Sep', 5)}")   # Expected Output: Spring
print(f"{get_season('Dec', 30)}")  # Expected Output: Winter
print(f"{get_season('Mar', 12)}")  # Expected Output: Winter
print(f"{get_season('Jun', 27)}")  # Expected Output: Spring
