import random
HANGMANPICS = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  0   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  0   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  0   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  0   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  0   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  0   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
 [0   |
 /|\  |
 / \  |
      |
=========''', '''
 +---+
  |   |
 [0]  |
 /|\  |
 / \  |
      |
=========''']

words = {'Colors': 'red orange blue black white brown silver crimson green yellow indigo violet pink purple'.split(),
         'Shapes': ' square triangle rectangle circle ellipse rhombus trapezoid chevron pentagon hexagon septagon octagon'.split(),
         'Fruits': 'apple orange lemon lime pear watermelon grape grapefruit cherry banana cantaloupe mango strawberry tomato'.split(),
         'Animals': 'bat bear beaver cat cougar crab deer dog donkey duck eagle fish frog goat leech lion lizard monkey moose mouse otter owl panda python rabbit rat shark sheep skunk squid tiger turkey turtle weasel whale wholf woombat zebra'.split()}


def getRandomWord(wordDict):
    wordKey = random.choice(list(wordDict.keys()))

    wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)

    return [wordDict[wordKey][wordIndex], wordKey]


def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end=' ')
    print()

def getGuess(aleadyGuessed):
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in aleadyGuessed:
            print('You have already guessed that letter. Please choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

def playAgain():
    print('Do you want to play again? y/n')
    return input().lower().startswith('y')

print('H A N G M A N')

difficulty = 'X'
while difficulty not in ['E', 'M', 'H']:
    print('Enter difficulty: E - Easy, M - Medium, H - Hard')
    difficulty = input().upper()
if difficulty == 'M':
    del HANGMANPICS[8]
    del HANGMANPICS[7]
if difficulty == 'H':
    del HANGMANPICS[8]
    del HANGMANPICS[7]
    del HANGMANPICS[6]
    del HANGMANPICS[5]

missedLetters = ''
correctLetters = ''
secretWord, secretSet = getRandomWord(words)
gameIsDone = False


while True:
    print('The secret word is in the set: ' + secretSet)
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        foundAllLetters= True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
                print('Yes! The secret word is "' + secretWord + '"! You have won!')
                gameIsDone = True
                if playAgain():
                    missedLetters = ''
                    correctLetters = ''
                    gameIsDone = False
                    secretWord, secretSet = getRandomWord(words)
                else:
                    break
    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(HANGMANPICS) - 1:
            displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True

            if gameIsDone:
                if playAgain():
                    missedLetters = ''
                    correctLetters = ''
                    gameIsDone = False
                    secretWord, secretSet = getRandomWord(words)
                else:
                    break


















