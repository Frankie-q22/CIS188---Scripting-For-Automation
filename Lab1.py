Name = input("Input Your Name: ")
print('Nice to meet you, ' + Name)
Age = int(input("How Old Are You?: "))


print(Name,  'if we add the number of letters in your name:', len(Name), ',to your age:', Age)
nextAge = (len(Name)) + Age
Xyears = nextAge - Age
print('You will be', nextAge, 'in', Xyears, 'years')

