import ceaserCipherlogo

alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y', 'z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y', 'z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y', 'z']

def ceaserCipher(choice,text, key):
    if choice=="Encode":
        encryptedText=""
        for letter in text:
            if letter in alphabets:
                getPos=alphabets.index(letter)
                newPos=getPos+key
                encryptedText+=alphabets[newPos]
            else:
                encryptedText+=letter
        print(f"Encrypted Text -> {encryptedText}")
    elif choice=="Decode":
        decryptedText=""
        for letter in text:
            if letter in alphabets:
                getPos=alphabets.index(letter)
                newPos=getPos-key
                decryptedText+=alphabets[newPos]
            else:
                decryptedText+=letter
        print(f"Decrypted Text -> {decryptedText}")

def getUserInput():
    userInput=str(input("Encode (E) - Decode (D) - Quit (Q) "))
    return userInput

def getUserText():
    userText=str(input("Text: ")).lower()
    return userText

def getUserKey():
    userKey=int(input("Shift: "))
    if userKey>26:
        userKey=userKey%26
        print(f"You have entered a key > 26. Your actual key is: {userKey}")
    return userKey

programStatus=False

print(ceaserCipherlogo.newLogo)

while programStatus==False:
    userInput=getUserInput()
    if userInput=="E" or userInput=="e":
        ceaserCipher("Encode",getUserText(),getUserKey())
    elif userInput=="D" or userInput=="d":
        ceaserCipher("Decode",getUserText(),getUserKey())
    elif userInput=="Q" or userInput=="q":
        programStatus=True
        print("Exiting ...")
