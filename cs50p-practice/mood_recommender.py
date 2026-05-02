# Day 3: Mood-Based Activity Recommender
# May 2, 2026

def mood_recommender(mood, energy):
    if mood >= 8 and energy == "high":
        return "You should go for a sprint!"
    elif mood >= 5 and energy == "medium":
        return "You should read, maybe?"
    elif mood >= 3 and energy == "low":
        return "You should take a short nap!"
    else:
        return "You should have some hot chocolate and marshmallows!"


print("Hello\n")
name = input("What's your name? ").strip()
mood = int(input(f"So, {name}, from a scale of 1-10, how are you feeling today? "))
energy = input("And how's your energy level? (high/medium/low) ").strip().lower()
print(mood_recommender(mood, energy))
