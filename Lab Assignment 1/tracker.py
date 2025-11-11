# Name : Sanskriti Rai
# Date : 27 Oct 2025
# Title : Building a Calorie Tracking Console App
# An app which helps you track your daily calories

print("Welcome to Daily Calorie Tracker")

n = int(input("Enter the number of meals: "))
dcl = int(input("Enter your daily calorie limit: "))

meal = []
cal = []
total = 0

for i in range(n):
    m = input("Enter your meal name: ")
    a = int(input("Enter the calorie amount of the meal: "))
    meal.append(m)
    cal.append(a)
    total += a

print("\nMeal Name      Calories")
print("-------------------------")
for i in range(n):
    print(f"{meal[i]}      {cal[i]}")

print("-------------------------")
print(f"Total:   {total}")
print(f"Average: {total/n}")


if total > dcl:
    print("Warning: Exceeding daily calorie limit!")
else:
    print("Under the daily calorie limit.")

import time

s = input("Do you want to save this report? (yes/no): ")

if s.lower() == "yes":
    timestamp = time.ctime()

    f = open("caloriereport.txt", "w")

    f.write("Daily Calorie Tracker Report\n")
    f.write("Time: " + timestamp + "\n")
    f.write("--------------------------------\n")
    f.write("Meal Name      Calories\n")
    f.write("--------------------------------\n")

    for i in range(n):
        f.write(f"{meal[i]}      {cal[i]}\n")

    f.write("--------------------------------\n")
    f.write(f"Total:   {total}\n")
    f.write(f"Average: {total/n}\n")

    if total > dcl:
        f.write("Warning: Exceeding daily calorie limit!\n")
    else:
        f.write("Under the daily calorie limit.\n")

    f.close()
    print("Report saved successfully as 'caloriereport.txt'")
else:
    print("Report not saved.")

