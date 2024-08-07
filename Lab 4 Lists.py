#Frankie Quintero
#This Program is a coin flip experiment which allows a user to basically flip a coin for a desired amount and check for a streak
#i couldve added an input number of instances function but the assignment asks or 10000 instances
import random

number_copies = 15  # Change this to the number of copies you want to print

#Checks if element is heads or tails, and if its consistent all the way through
def check_streak(lst, element, streak_length):
    count = 0
    for item in lst:
        if item == element:
            count += 1
            if count == streak_length:
                return True
        else:
            count = 0
    return False
#A list is created every 6 instances in order to keep it parallel with the streak amount
#the instances are actually 0s and 1s, but are converted to strings
streak_checker = 0
for _ in range(number_copies):
    try_list = []  # Create a new empty list for each copy

    for i in range(6):
        HeadsorTails = random.randint(0, 1)
        if HeadsorTails == 0:
            try_list.append('T')
        else:
            try_list.append('H')

    print(try_list)

    #If a streak of heads or tails is found, it will print out where the streak is found and which side its landed on
    
    if check_streak(try_list, 'H', 6):
        streak_checker = streak_checker + 1
        print("Found a streak of 6 consecutive 'H'")
    if check_streak(try_list, 'T', 6):
        streak_checker = streak_checker + 1
        print("Found a streak of 6 consecutive 'T'")
        
#Prints out the information at the end       
print("===============================================================================================================================================================")    


Percent_Ratio = streak_checker/number_copies * 100
Streak_Ratio = streak_checker/number_copies 
instances = number_copies * 6

Number = Percent_Ratio
number = Streak_Ratio

decimal_places = 3
Formatted_number = f"{Number:.{decimal_places}f}"
formatted_number = f"{number:.{decimal_places}f}"

print("Instances: ", instances)
print('----------------------')
print("Instances Per List: 6")
print('----------------------')
print("Lists Created: ", number_copies)
print('----------------------')
print("Streaks Detected: ",streak_checker)
print('----------------------')
print("There Was A", Formatted_number,"% Chance To Get A Streak" )
print('--------------------------------------------')
print("Just To Scale It: ")
print("Only",formatted_number, "Out Of 100" )
print('\n')