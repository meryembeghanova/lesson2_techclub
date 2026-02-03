import random
from datetime import date

# Feature added with AI help: random motivational quotes
quotes = [
    "Small steps every day lead to big results.",
    "Discipline is choosing what you want most.",
    "Your future self will thank you.",
    "Progress, not perfection.",
    "One week can change everything."
]

print("🌟 Weekly Goals Tracker 🌟")

# Choose a random motivational quote
quote = random.choice(quotes)
print("\nMotivational Quote of the Week:")
print(f"\"{quote}\"\n")

# Ask how many goals
while True:
    try:
        num_goals = int(input("How many goals do you want to set for this week? (3-5): "))
        if 3 <= num_goals <= 5:
            break
        else:
            print("Please enter a number between 3 and 5.")
    except ValueError:
        print("Please enter a valid number.")

# Store goals in a list
goals = []

for i in range(num_goals):
    goal = input(f"Enter goal {i + 1}: ")
    goals.append(goal)

# Get today's date
today = date.today()

# Save goals to a file
filename = "weekly_goals.txt"
with open(filename, "w") as file:
    file.write("WEEKLY GOALS TRACKER\n")
    file.write(f"Week starting: {today}\n\n")
    file.write("Motivational Quote:\n")
    file.write(f"\"{quote}\"\n\n")
    file.write("Your Goals:\n")

    for goal in goals:
        file.write(f"☐ {goal}\n")

print(f"\n✅ Your goals have been saved to '{filename}'")
print("Good luck with your week! 💪")
