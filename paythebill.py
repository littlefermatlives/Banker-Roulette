import random
print("Welcome to the Banker Roulette - Who will pay the bill?")
number_of_person = int(input("Number of Person present in group\n"))
names_string = input("Enter names of persons\n")
names = names_string.split(", ")
r = random.randint(1,number_of_person)
print(f"Today {names[r-1]} should pay the bill")