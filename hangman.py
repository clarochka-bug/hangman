import random

file = open('words.txt')
contents = file.read()
file.close()

contents = contents.split('\n')
contents.pop()
#reading word list (2), splitting it up (5), removing last time (6)

contents_length = len(contents)
random_index = random.randint(0, (contents_length-1))

random_word = contents[random_index]

length_word = len(random_word)

list_random_word = list(random_word)

guessed = ("_" * length_word)

guessed_list = list(guessed)

lives = 10
list_wrong_letter = []
list_right_letter = []


gameDone = False 
while gameDone == False:

    print("\n")

    print(guessed_list)
    print(f'the letters you have guessed incorrectly are {list_wrong_letter}')

    print(f'You have {lives} lives left')
    letter = input("Please enter a letter: ")

    guessed_correctly = False 

    for x in range(len(list_random_word)): 
        if letter == list_random_word[x]:
            guessed_list[x] = list_random_word[x]
            guessed_correctly = True 

    if guessed_correctly == False: 
        lives -= 1 
        list_wrong_letter.append(letter)
        

    
    if lives == 0: 
        gameDone = True 
        print(f"you lost!! the word was {random_word}")
    if guessed_list == list_random_word: 
        gameDone = True 
        print(f"slay queen you win!!! the word was {random_word}")

    
