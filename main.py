import random
print('Welcome to Rock, Paper, and Scissors Tournament.')
print('Do you have what it takes to win!')
print('R is for "Rock", P is for "Paper" and S is for "Scissors".')

gameChoices = ['R','P','S']
cpuChoice = random.choice(gameChoices)
playerChoice = input('Please enter a letter to proceed : ').upper()
while playerChoice not in gameChoices:
        playerChoice = input('!!! Please enter a valid letter to proceed : ').upper()

while playerChoice == cpuChoice:
    print("It's a Tie !!!!")
    playerChoice = input('!!! Please enter a letter to try again : ').upper()
    while playerChoice not in gameChoices:
        playerChoice = input('!!! Please enter a valid letter to proceed : ').upper()

else:
        if playerChoice == 'R' and cpuChoice == 'S':
            print('Player (Rock) : CPU (Scissors)')
            print('Player Wins !!!!')
            
        elif playerChoice == 'R' and cpuChoice == 'P':
            print('Player (Rock) : CPU (Paper)')
            print('CPU Wins !!!!')
            
        elif playerChoice == 'S' and cpuChoice == 'R':
            print('Player (Scissors) : CPU (Rock)')
            print('CPU Wins !!!!')

        elif playerChoice == 'S' and cpuChoice == 'P':
            print('Player (Scissors) : CPU (Paper)')
            print('Player Wins !!!!')

        elif playerChoice == 'P' and cpuChoice == 'S':
            print('Player (Paper) : CPU (Scissors)')
            print('CPU Wins !!!!')

        elif playerChoice == 'P' and cpuChoice == 'R':
            print('Player (Paper) : CPU (Rock)')
            print('Player Wins !!!!')
