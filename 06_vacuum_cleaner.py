# Program 6: Vacuum Cleaner Problem
rooms = {"A": "Dirty", "B": "Dirty"}
location = "A"
while "Dirty" in rooms.values():
    if rooms[location] == "Dirty":
        print("Cleaning room", location)
        rooms[location] = "Clean"
    else:
        location = "B" if location == "A" else "A"
        print("Moving to room", location)
print("All rooms are clean:", rooms)

