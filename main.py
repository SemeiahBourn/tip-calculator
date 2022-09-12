#If the bill was $150.00, split between 5 people, with 12% tip. 
print("Welcome to the Tip Calculator.\n")
bill = float(input("Whats was the total bill?"))

tip= input("What percentage would you like to give? 10,12, or 15?")
new_tip= int(tip) / 100
people = int(input("How many people to split the bill between?"))
bill_with_tip = new_tip * bill + bill

bill_per_person = bill_with_tip / people
total = "{:.2f}".format(bill_per_person)
print(f"Each person would pay ${total}")
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇