
# Name: Jason Noyola
# Date: 11/01/2026
# Assignment: P4HW1
# Description: Calculate the average score after
# removing the lowest score and assign a letter grade.

scores = []

num_scores = int(input("How many scores do you want to enter? "))

while num_scores <= 0:
    print("Please enter a number greater than 0.")
    num_scores = int(input("How many scores do you want to enter? "))

for i in range(num_scores):
    score = float(input(f"Enter score #{i + 1}: "))

    while score < 0 or score > 100:
        print("INVALID Score entered!!!")
        print("Score should be between 0 and 100")
        score = float(input(f"Enter score #{i + 1} again: "))

    scores.append(score)

# Find and remove the lowest score
lowest_score = min(scores)
scores.remove(lowest_score)

# Calculate the average after dropping the lowest score
if len(scores) > 0:
    average = sum(scores) / len(scores)
else:
    average = 0

# Determine letter grade
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

# Display results
print("\n---------- Results ----------")
print(f"Lowest Score : {lowest_score}")
print(f"Score List   : {scores}")
print(f"Scores Average: {average:.2f}")
print(f"Grade        : {grade}")
