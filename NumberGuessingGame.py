#Import the random function
import random

#Output
print(' -=-=-=-=-=-=-=-=-=-=-=-=-= ')
print('|                          |')
print('|     Guessing  Number     |')
print('|                          |')
print(' -=-=-=-=-=-=-=-=-=-=-=-=-= ')

#Random number
numRand = random.randrange(1, 101)
#print(numRand)

replay = 'y'


#While loop
while replay == 'y':
    #Input
    num = int(input('\nChoose a number between 1 and 100: '))
    i = 1

    while num != numRand:
        if num > numRand:
            print('Your choice was too high')
            num = int(input('Try again: '))
        elif num < numRand:
            print('Your choice was too low')
            num = int(input('Try again: '))
        i += 1


    print('\nBINGO')
    print(f'Congratulations, the number {num} is correct!')
    print(f'You tried {i} times\n')
    
    replay = str(input('Do you wanna play again (y/n):'))
    if replay == 'y':
        continue
    elif replay == 'n':
        replay = False

print('\nThanks for playing')