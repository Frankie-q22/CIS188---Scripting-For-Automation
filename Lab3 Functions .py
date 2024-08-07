#Frankie Quintero
#Collatz sequence, A Mathmatical equation that has baffled Mathematicians for years 
# as it always ends up with the same answer no matter which number is first used for the equation

#defines the function of the collatz sequence in real life
def collatz(x):
    if x == 1:
        print("Here Is The Collatz Sequence")
    elif x % 2 == 0:
        print(int(x / 2))
        collatz(x / 2)
    else:
        print(int(x * 3 + 1))
        collatz(x * 3 + 1)

#Added Input validation (a habit which my CIS131 teacher got me accustomed to)
try:
    collatz(int(input('Choose a number greater than 1: ')))
except ValueError:
    print('Thats not a number, try again')
