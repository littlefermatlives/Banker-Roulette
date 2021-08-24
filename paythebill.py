import random
print("Welcome to the Banker Roulette - Who will pay the bill?")
number_of_person = int(input("Number of Person present in group\n"))
names_string = input("Enter names of persons\n")
names = names_string.split(", ")
#random_choice = random.rand(int(0,number_of_person-1))
#person_who_will_pay = names[random_choice]
r = random.choice(names)
print(f"Today {r} should pay the bill")
