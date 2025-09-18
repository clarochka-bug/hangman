import random

file = open('words.txt')
contents = file.read()
file.close()

contents = contents.split('\n')
contents.pop()
#reading word list, splitting it up (\n starts a new line), removing last item on list (bc it was an empty space)

contents_length = len(contents)
random_index = random.randint(0, (contents_length-1))
#choose a random index between 0 and 1000 (bc that is the amount of items in the list), also -1 bc computers start counting at 0 

random_word = contents[random_index]
#chooses a random word from the list of words 

length_word = len(random_word)
#determines length of the random word that was picked 

list_random_word = list(random_word)

guessed = ("_" * length_word)

guessed_list = list(guessed)
#creates a section '_ _ _ _ _' (with the amount of dashes that the word is), and also turns the characters 
# in the given word and the dashes into lists (which makes it easier to work with later)

lives = 10
list_wrong_letter = []
list_right_letter = []


gameDone = False 
while gameDone == False:
    #while game is not done we do the following actions: new line, print "_ _ _ _ _", 
    # print the incorrectly guessed letters, print the amount of lives left, user input to enter a letter, 


    print("\n")

    print(guessed_list)
    print(f'the letters you have guessed incorrectly are {list_wrong_letter}')

    print(f'You have {lives} lives left')
    letter = input("Please enter a letter: ")

    #in the section below, we determine if the guess is correct or not. 

    guessed_correctly = False 
    #here we assume it's false. 

    for x in range(len(list_random_word)): 
        if letter == list_random_word[x]:
            guessed_list[x] = list_random_word[x]
            guessed_correctly = True 
    #we check for presence of guessed letter in the letter list. 

    if guessed_correctly == False: 
        lives -= 1 
        list_wrong_letter.append(letter)
    #if remains false, we deduct life, and add letter to the 'wrong letter list'. 
        

    
    if lives == 0: 
        gameDone = True 
        print(f"you lost!! the word was {random_word}")
        #this is what happens if you lose the game. the game is done, and that happens when lives = 0. 
        #while loop = runs on condition 
    if guessed_list == list_random_word: 
        gameDone = True 
        print(f"slay queen you win!!! the word was {random_word}")
        #same thing but you win. both say the random word 

        

    
