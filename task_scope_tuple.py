# Task 1
# Write a program that asks the user to enter an integer and convert it to an int. The program should have 2 functions.
#     # The first function should ask the user to input information and return inputted value. 
#     # The second function receives the inputted value and converts it to int. 
# # If the user enters something that is not an integer, this function should catch an error and ask the user to enter an integer again. 
# # if the user inputs an integer, the program should print this number and quit w/o any error.



def get_number():
    number = input('Enter the number:')
    return(number)    

 
def convert_int():

 while True:
   try:
         number = int(get_number())
         print(number)
         break
   except ValueError:
         print("That was not an integer, try again")

convert_int()



#  Task 2
# Write a program that asks user to input a string and an integer `n`. 
# The Program should have 2 functions.
#  The first function should ask user to enter string and integer. 
#  The second function should receive the inputted value and print the character at index `n`.
# If the user enters wrong value, this function should catch an error and provide a proper error message with an explanation. 
# After the error is handled, the program should ask the user to enter a string and an integer again. 
# If user inputs a string and an integer, program should print the character at index `n` and quit w/o any error.


def from_user():
 while True:
   try:
         text = input('Enter the text:')
         number = int(input('Enter the number:'))
         return text, number
   except ValueError:
         print("That was not an integer, try again")


def index_text_i():
 while True:
   text, number = from_user()
   max_number = len(text)
   if number < max_number:
    i = text[number]
    print(i)
    break
   else:
    print(f"Your number {number} is out of bounds of the text, try again")


index_text_i()



# # # TASK 3
# # Transaction

balance = 5

def transaction(amount, type_ransaction):

    def deposit(amount):
        new_balance = balance + amount
        return(f'Your new balance is (when you add {amount}): {new_balance}')

    def withdrawal(amount):
        if balance < amount:
         return 'You don`t have this amount'
        else:
         new_balance = balance - amount
         return(f'Your new balance is (when you took out {amount}): {new_balance}')

  
    if type_ransaction == 'deposit': 
      print(deposit(amount))
    elif type_ransaction == 'withdrawal':
      print(f'{withdrawal(amount)}')


transaction(5, 'withdrawal')


# Task 4

import random

def dice_roll():
   roll_dice = random.randint(1, 6)
   return roll_dice

dice_roll()


# Task 5
# Use the function from the previous task to simulate 1000 dice rolls and print the result. 
# Calculate the number of times each number was rolled.

import random

dice_side = [0, 0, 0, 0, 0, 0]

for i in range(1000):
    roll_dice = dice_side.append(random.randint(1, 6))
    if roll_dice in dice_side:
        dice_side[roll_dice+1] += 1

print(f'side - count') 
for i in range(6):
    print(f'{i+1}   -   {dice_side.count(i+1)}')




# Task 6
# Simulate an election for two candidates. # The program should take 
#  the number of regions and
#  the rating for 1st candidate in each region (in percentage). 
# The program should run elections in every region. 
# In every region, the program should ask 10 000 voters. 
# Use the random module to simulate a voice from a person.
#  The candidate counts as a winner if he gains more than 50% of all votes. 
# The program should print the result of the election for each region and the winner

import random

def get_rating(region_index): 
 while True:
        rating = float(input(f'Enter the rating (from 0 to 100) for Candid_1 in Region:{region_index + 1}: '))
        if 0 <= rating <= 100:
          return rating
        else:
          print('Please check your number, should be between 0 and 100!')


def simulate_election(count_reg, candid_1_rating):

   all_votes = count_reg * 10000
   cand_1_all_votes = 0

   for i in range(1, count_reg + 1):
      region_votes = 10000
      cand_1_votes = sum(1 for _ in range(region_votes) if random.randint(0, 100) <= candid_1_rating[i - 1])
      cand_1_all_votes += cand_1_votes

      cand_1_percent = (cand_1_votes / region_votes) * 100
      cand_2_percent = 100 - cand_1_percent
      
      print(f'In Region {i}, percentages between candidates:')
      print(f'Candidate 1: {cand_1_percent} %')
      print(f'Candidate 2: {cand_2_percent} %')

   cand1_all_reg_percent = (cand_1_all_votes / all_votes) * 100
   cand2_all_reg_percent = 100 - cand1_all_reg_percent

   print('Based on all regions:')
   print(f'Candidate 1: {cand1_all_reg_percent}  % overall')
   print(f'Candidate 2: {cand2_all_reg_percent} % overall')

   if cand_1_all_votes > all_votes / 2:
      print('Candidate 1 won!')
   else:
      print('Candidate 2 won!')


def main():
   count_reg = int(input('Enter number of regiones:'))
   candid_1_rating = [get_rating(i) for i in range(count_reg)]

   simulate_election(count_reg, candid_1_rating)


main()