import random
import time

BOARD = ['''
  _________.___________
  |--------(---------||
           )         ||
           (         ||
                     ||
                     ||
                     ||
                     ||
                     ||
                     ||
                     ||
                     ||
                     ||
                     ||
                     ||
                     ||
                     ||
                     ||
                     ||
|=====================|
=======================''','''
  _________.___________
  |--------(---------||
           )         ||
           (         ||
         ~~~~~       ||
        (     )      ||
        o_   _o      ||
          \ /        ||
                     ||
                     ||
                     ||
                     ||
                     ||
                     ||
                     ||
                     ||
                     ||
                     ||
                     ||
|=====================|
=======================''','''
  _________.___________
  |--------(---------||
           )         ||
           (         ||
         ~~~~~       ||
        ( @ @ )      ||
        o_ ^ _o      ||
          \-/        ||
                     ||
                     ||
                     ||
                     ||
                     ||
                     ||
                     ||
                     ||
                     ||
                     ||
                     ||
|=====================|
=======================''','''
  _________.___________
  |--------(---------||
           )         ||
           (         ||
         ~~~~~       ||
        ( @ @ )      ||
        o_ ^ _o      ||
          \-/        ||
          =+=        ||
          | |        ||
          | |        ||
          | |        ||
          ===        ||
                     ||
                     ||
                     ||
                     ||
                     ||
                     ||
|=====================|
=======================''','''
  _________.___________
  |--------(---------||
           )         ||
           (         ||
         ~~~~~       ||
        ( @ @ )      ||
        o_ ^ _o      ||
          \-/        ||
          =+=        ||
         /| |        ||
        / | |        ||
       /  | |        ||
          ===        ||
                     ||
                     ||
                     ||
                     ||
                     ||
                     ||
|=====================|
=======================''','''
  _________.___________
  |--------(---------||
           )         ||
           (         ||
         ~~~~~       ||
        ( @ @ )      ||
        o_ ^ _o      ||
          \-/        ||
          =+=        ||
         /| |\       ||
        / | | \      ||
       /  | |  \     ||
          ===        ||
                     ||
                     ||
                     ||
                     ||
                     ||
                     ||
|=====================|
=======================''','''
  _________.___________
  |--------(---------||
           )         ||
           (         ||
         ~~~~~       ||
        ( @ @ )      ||
        o_ ^ _o      ||
          \-/        ||
          =+=        ||
         /| |\       ||
        / | | \      ||
       /  | |  \     ||
          ===        ||
         //          ||
        //           ||
                     ||
                     ||
                     ||
                     ||
|=====================|
=======================''','''
  _________.___________
  |--------(---------||
           )         ||
           (         ||
         ~~~~~       ||
        ( @ @ )      ||
        o_ ^ _o      ||
          \-/        ||
          =+=        ||
         /| |\       ||
        / | | \      ||
       /  | |  \     ||
          ===        ||
         // \\\\       ||
        //   \\\\      ||
                     ||
                     ||
                     ||
                     ||
|=====================|
=======================''','''
  _________.___________
  |--------(---------||
           )         ||
           (         ||
         ~~~~~       ||
        ( @ @ )      ||
        o_ ^ _o      ||
          \-/        ||
          =+=        ||
         /| |\       ||
        / | | \      ||
       /  | |  \     ||
          ===        ||
         // \\\\       ||
        //   \\\\      ||
       <_)           ||
                     ||
                     ||
                     ||
|=====================|
=======================''','''
  _________.___________
  |--------(---------||
           )         ||
           (         ||
         ~~~~~       ||
        ( X X )      ||
        o_ ^ _o      ||
          \-/        ||
          =+=        ||
         /| |\       ||
        / | | \      ||
       /  | |  \     ||
          ===        ||
         // \\\\       ||
        //   \\\\      ||
       <_)   (_>     ||
                     ||
                     ||
                     ||
|=====================|
=======================''']

words = {'nouns':'accused addiction alligator amazement anchovies assassination backing bandit bedroom bump buzzers courtship critic dauntless dawn design dickens discontent embrace employer engagements excitements exposure eyeball fixture futurity glow gust hint immediacy investments kickshaws leapfrog luggage manager mimic misgiving mountaineer ode outbreak pageantry pedant perusal questioning reinforcement retirement roadway rumination savagery scuffles shudders switch tardiness transcendence urging watchdog wormhole zany'.split(),
'adjectives':'aerial auspicious baseless beached bloodstained blushing circumstantial consanguineous deafening disgraceful domineering enrapt epileptic equivocal eventful fashionable foregone frugal generous gloomy gnarled hush inaudible invulnerable jaded juiced lackluster laughable lonely lustrous madcap majestic marketable monumental nervy noiseless oscene olympian premeditated promethean quarrelsome radiance rancorous reclusive remorseless rival sacrificial sanctimonious softhearted splitting stealthy traditional tranquil unmitigated unreal varied vaulting viewless widowed worthless yelping'.split(),
'verbs':'besmirch bet blanket cake cater champion compromise cow denote deracinate dialogue dislocate divest drug dwindle elbow enmesh film forward gossip grovel hobnob humour hurry impedes jet jig label lapse lower misquote negotiate numb pander partner petition puke rant reword secure submerge swagger torture unclog'.split(),
'adverbs':'importantly instinctively obsequiously threateningly tightly trippingly unaware'.split()}

def chooseFromDict(wordDict):
    chosenKey = random.choice(list(wordDict.keys()))
    chosenWord = random.choice(wordDict[chosenKey])
    return chosenKey, chosenWord

def chooseAWord(wordList):
    wordIndex = random.randint(0,len(wordList)-1)
    chosenWord = wordList[wordIndex]
    return chosenWord

def showTheBoard(board, chosenWord, guessedLetters, missedLetters):
    blanks = '_' * len(chosenWord)
    lettersLeft = ''
    print(board[len(missedLetters)])
    for each in range(len(chosenWord)):
        if chosenWord[each] in guessedLetters:
            blanks = blanks[:each] + chosenWord[each] + blanks[each+1:]
        elif chosenWord[each] not in guessedLetters:
            if chosenWord[each] not in lettersLeft:
                lettersLeft = lettersLeft + chosenWord[each]
    print(' ' *(int((24-(len(blanks)*2))/2)),end='')
    for each in range(len(blanks)):
        print (blanks[each] + ' ', end='')
    print()
    print()
    print('Bad guesses: ', end='')
    for each in range(len(missedLetters)):
        if len(missedLetters) > 1:
            if each < len(missedLetters)-1:
                print(missedLetters[each] + ', ', end='')
            else:
                print(missedLetters[each], end='')
        else:
            print(missedLetters[each], end='')
    print()
    print()
    return lettersLeft
    

def playTheGame(board, wordDict, playNow):
    while playNow == True:
        chosenKey, chosenWord = chooseFromDict(wordDict)
        guessedLetters = ''
        missedLetters = ''
        gameOver = False
        print('H A N G   T H E   M A N : ' + chosenKey.upper())
        while gameOver == False:
            lettersLeft = showTheBoard(board, chosenWord, guessedLetters, missedLetters)
            print('Guess a letter: ', end='')
            newGuess = input().lower()
            while True:
                if len(newGuess) > 1:
                    print()
                    print('Guess ONE letter: ', end='')
                    newGuess = input().lower()
                elif newGuess in guessedLetters:
                    print()
                    print('Guess a NEW letter: ', end='')
                    newGuess = input().lower()
                elif newGuess not in 'abcdefghijklmnopqrstuvwxyz':
                    print()
                    print('Guess a LETTER: ', end='')
                    newGuess = input().lower()
                elif newGuess in chosenWord:
                    print()
                    print('Yup! \'' + newGuess + '\'  is in the secret word', end='')
                    guessedLetters = guessedLetters + newGuess
                    time.sleep(0.5)
                    print('.', end='')
                    time.sleep(0.5)
                    print('.', end='')
                    time.sleep(0.5)
                    print('.', end='')
                    time.sleep(0.5)
                    print()
                    print()
                    if newGuess == lettersLeft:
                        gameOver = True
                    break
                elif newGuess not in chosenWord:
                    print()
                    print('Sorry, \'' + newGuess +'\' isn\'t in the secret word', end='')
                    guessedLetters = guessedLetters + newGuess
                    missedLetters = missedLetters + newGuess
                    time.sleep(0.5)
                    print('.', end='')
                    time.sleep(0.5)
                    print('.', end='')
                    time.sleep(0.5)
                    print('.', end='')
                    time.sleep(0.5)
                    print()
                    print()
                    if len(missedLetters) >= (len(board) - 1):
                        gameOver = True
                    break
        if len(missedLetters) >= (len(board) - 1):
            showTheBoard(board, chosenWord, guessedLetters, missedLetters)
            print('Hanged! Sorry about that. The word was \'' + chosenWord + '.\'')
            print()
            print('Play again? (yes / no): ', end='')
            playAgain = input().lower()
            while True:
                if playAgain[0] == 'y':
                    print()
                    print('Great! Just one second', end='')
                    time.sleep(0.5)
                    print('.', end='')
                    time.sleep(0.5)
                    print('.', end='')
                    time.sleep(0.5)
                    print('.')
                    print()
                    time.sleep(0.5)
                    break
                elif playAgain[0] == 'n':
                    print()
                    print('Sorry to hear that. Come back again later!')
                    playNow = False
                    break
                else:
                    print()
                    print('Please answer yes or no: ', end='')
                    playAgain = input()
        else:
            showTheBoard(board, chosenWord, guessedLetters, missedLetters)
            print('You win! Congratulations, the word was \'' + chosenWord + '.\'')
            print()
            print('Play again? (yes / no): ', end='')
            playAgain = input().lower()
            while True:
                if playAgain[0] == 'y':
                    print()
                    print('Great! Just one second', end='')
                    time.sleep(0.5)
                    print('.', end='')
                    time.sleep(0.5)
                    print('.', end='')
                    time.sleep(0.5)
                    print('.')
                    print()
                    print()
                    time.sleep(0.5)
                    break
                elif playAgain[0] == 'n':
                    print()
                    print('Sorry to hear that. Come back again later!')
                    playNow = False
                    break
                else:
                    print()
                    print('Please answer yes or no: ', end='')
                    playAgain = input()

play = True
playTheGame(BOARD, words, play)
