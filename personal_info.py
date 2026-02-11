# Personal Information Manager
# My first Python project
#Name: Srimayi G

# Welcome message
print("=" * 40)
print("    PERSONAL INFORMATION MANAGER")
print("=" * 40)
print()

# Store static information
name = "Alex Johnson"
age = 22
city = "San Francisco"
hobby = "playing guitar"

# Get user input
print("Please tell me about yourself:")
print("-" * 30)

Name = input("What's your Name? ")
while Name == "":
    print("Please enter a valid name!")
    Name = input("What's your Name? ")

Age = input("What's your Age? ")
while Age == "":
    print("Please enter a valid age!")
    Age = input("What's your age? ")

   
favorite_food = input("What's your favorite food? ")
while favorite_food == "":
    print("Please enter a valid food!")
    favorite_food = input("What's your favorite food? ")

favorite_color = input("What's your favorite color? ")
while favorite_color == "":
    print("Please enter a valid color!")
    favorite_color = input("What's your favorite color? ")

City = input("What's your City? ")
while city == "":
    print("Please enter a valid city name!")
    City = input("What's your City? ")

Hobby = input("What's your Hobby? ")
while Hobby == "":
    print("Please enter your Hobby!")
    Hobby = input("What's your Hobby? ")

# Calculate age in months
age_in_months = age * 12

# Display all information
print()
print("=" * 40)
print("        YOUR INFORMATION")
print("=" * 40)
print()

print(f"Name: {Name}")
print(f"Age: {Age} years ({age_in_months} months old)")
print(f"City: {City}")
print(f"Hobby: {Hobby}")
print()
print(f"Favorite Food: {favorite_food}")
print(f"Favorite Color: {favorite_color}")
print()

# Goodbye message
print("=" * 40)
print("Thanks for using this program!")
print("=" * 40)
