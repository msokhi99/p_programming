import random
import hangmanWords
import hangmanStages

wordChosen=random.choice(hangmanWords.words)

guessList=[]
for i in range(len(wordChosen)):
    guessList.append("_")
print(guessList)

totalLives=6
gameOverStatus=False

print(''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
      ''')

while gameOverStatus==False:
    userGuess=str(input("Guess a word: "))
    if userGuess in guessList:
        print(f"\nYou have already guessed the letter {userGuess}")
    for index in range(len(wordChosen)):
        letter=wordChosen[index]
        if userGuess==letter:
            guessList[index]=letter
    
    print(f"\n{guessList}")

    if userGuess not in wordChosen:
        totalLives-=1
        print(f"\nLetter {userGuess} is not in the word. You have {totalLives} lives left.")
        if totalLives==0:
            print(f"Game Over.\nThe word was {wordChosen}.")
            gameOverStatus=True
    if "_" not in guessList:
        print("You won.")
        gameOverStatus=True
    
    print(hangmanStages.stageOfGame[totalLives])
