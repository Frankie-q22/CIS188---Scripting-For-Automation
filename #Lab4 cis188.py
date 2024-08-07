#Lab4 cis188
import random


ry_list = [0 for i in range(6)]
num_copies = 50  # Change this to the number of copies you want to print

for _ in range(num_copies):
    print(ry_list)




for i in range(100):
 HeadsorTails = random.randint(0,1)
 if HeadsorTails == 0:
  ry_list.append('T')
 if HeadsorTails == 1:
  ry_list.append('H')
print("=======================================================================================================================")

number_copies = 50  # Change this to the number of copies you want to print

for _ in range(number_copies):
    try_list = []  # Create a new empty list for each copy

    for i in range(6):
        HeadsorTails = random.randint(0, 1)
        if HeadsorTails == 0:
            try_list.append('T')
        else:
            try_list.append('H')

    print(try_list)
    
print("=======================================================================================================================")
print("=======================================================================================================================")
print("=======================================================================================================================")

import random

number_copies = 100  # Change this to the number of copies you want to print

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

for _ in range(number_copies):
    try_list = []  # Create a new empty list for each copy

    for i in range(6):
        HeadsorTails = random.randint(0, 1)
        if HeadsorTails == 0:
            try_list.append('T')
        else:
            try_list.append('H')

    print(try_list)

    streak_checker = 0
    if check_streak(try_list, 'H', 6):
        streak_checker = streak_checker =+ 1
        print("Found a streak of 6 consecutive 'H'")
    if check_streak(try_list, 'T', 6):
        streak_checker = streak_checker =+ 1
        print("Found a streak of 6 consecutive 'T'")
        
        
    
    print("Amount Of Streaks: ", streak_checker)