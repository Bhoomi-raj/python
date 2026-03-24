# Step 1: Create a SET of car components
components = {"Engine", "Battery", "Brake", "Radiator"}

print("All Components:", components)


# Step 2: Create a DICTIONARY to store status
status = {
    "Engine": "Working",
    "Battery": "Working",
    "Brake": "Not Working",
    "Radiator": " Working"
}

print("\nComponent Status:")
for part in status:
    print(part, ":", status[part])


# Step 3: Check if any component is not working
for part in status:
    if status[part] == "Not Working":
        print("\n⚠ Problem found in:", part)