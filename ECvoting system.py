#EC voting eligibility system
Name = input('Enter your name:')
Age = int(input('Énter your age:'))
Nationality = input('Enter your nationality:').lower()
 # checks if person meets the requirments
if Age >= 18 and Nationality == "ghanaian":
    print(f" {Name} you are eligible to vote")
else :
    print(f" {Name} you are not eligible to vote")
