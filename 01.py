from datetime import date

# Get today's date
today = date.today()
formatted_date = today.strftime("%B %d, %Y")

# Ask questions (9 total)
name = input("What is your name? ")
age = input("How old are you? ")
country = input("Which country do you live in? ")
favorite_song = input("What is your favorite song right now? ")
favorite_subject = input("What is your favorite school subject? ")
biggest_goal = input("What is your biggest goal right now? ")
best_friend = input("Who is your best friend? ")
current_hobby = input("What is your favorite hobby? ")
future_message = input("Write a message to your future self: ")

# Format content using f-strings
content = f"""
========================================
           TIME CAPSULE - 2026
        Created: {formatted_date}
     To be opened in: Feb 2, 2030
========================================

Name: {name}
Age: {age}
Country: {country}

Favorite Song: {favorite_song}
Favorite Subject: {favorite_subject}
Biggest Goal: {biggest_goal}
Best Friend: {best_friend}
Favorite Hobby: {current_hobby}

Message to Future Me:
{future_message}

========================================
"""

# Write to file
with open("time_capsule_2026.txt", "w", encoding="utf-8") as file:
    file.write(content)

print("✅ Your time capsule has been saved successfully!")
