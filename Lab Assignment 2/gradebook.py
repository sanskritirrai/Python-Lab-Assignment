# Name : Sanskriti Rai
# Date : 9 Nov 2025
# Title : Building a Grade Book Analyzer
# An app which analyzes grades

import csv
import statistics

print("Welcome to Gradebook Analyzer!")
print("1. Manual Entry")
print("2. Load from CSV")

choice = input("Enter your choice (1 or 2): ")

marks = {}

if choice == "1":
    while True:
        name = input("Enter student name (or 'done' to stop): ")
        if name.lower() == "done":
            break
        marks[name] = float(input("Enter marks: "))
elif choice == "2":
    file = input("Enter CSV filename (e.g. data.csv): ")
    with open(file, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            marks[row["Name"]] = float(row["Marks"])
avg = sum(marks.values()) / len(marks)
med = statistics.median(marks.values())
high = max(marks.values())
low = min(marks.values())

print(f"\nAverage: {avg:.2f}")
print(f"Median: {med}")
print(f"Highest: {high}")
print(f"Lowest: {low}")

grades = {}
for n, m in marks.items():
    if m >= 90: g = "A"
    elif m >= 80: g = "B"
    elif m >= 70: g = "C"
    elif m >= 60: g = "D"
    else: g = "F"
    grades[n] = g

passed = [n for n, m in marks.items() if m >= 40]
failed = [n for n, m in marks.items() if m < 40]

print("\nName\tMarks\tGrade")
print("---------------------------")
for n in marks:
    print(f"{n}\t{marks[n]}\t{grades[n]}")

print("\nGrade Count:")
for g in ['A','B','C','D','F']:
    print(g, "=", list(grades.values()).count(g))

print(f"\nPassed ({len(passed)}): {', '.join(passed)}")
print(f"Failed ({len(failed)}): {', '.join(failed)}")
