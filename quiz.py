#! python3

easy_question="""
    The Revolutionary War in America lasted from year ___1___ until 1783.
    ___2___ was elected as general by the Continental Congress in the city of
    ___3___, where he was then tasked with traveling to ___4___ to fight the
    regulars.\n"""

medium_question="""The second President of the United States of America was
    ___1___, who was the first Vice President. He was a graduate of ___2___
    University, studying law. Originally from ___3___, Massachusetts
    (In a section known as Braintree) he became a delegate and pushed for the
    colonies to seek their independence from Great Britain. Out of his many
    accomplishments as a founding father he was most noted for his creation of
    the rules and regulations forming the United States ___4___.\n"""

difficult_question="""The Battle of ___1___ was a significant battle in the
    Revolutionary War that actually took place on ___2___. Taking place on the
    month and day of ___3___ in 1775 some ___4___ British troops marched, but
    were repelled three times by the Colonial forces.\n"""

blank_index=["__1___"," ___2___", "___3___", "___4___"]

easy_answer=["1775","George Washington","Philadelphia","Boston"]
medium_answer=[ "John Adams","Harvard","Quincy","Navy"]
difficult_answer=[ "Bunker Hill","Breed's Hill", "July 17","2,200"]

level_of_difficulty_dictionary = {
    "easy":(easy_question, easy_answer),
    "medium":(medium_question, medium_answer),
    "hard":(difficult_question,difficult_answer)}

number_of_questions = int(len(blank_index))

def difficulty_level():
    level = input(
        r'Please select the level of difficulty of easy, medium or hard: ')
    level = level.lower()
    if level in level_of_difficulty_dictionary:
        return level_of_difficulty_dictionary[level]
    else:
        print ('Please type easy, medium or hard\n')
        difficulty_level()

def quiz_question(difficulty_level):
    fill_in_blank_question, fill_in_blank_answer = difficulty_level()
    turns = int(input("How many number of turns would you like: "))
    print (fill_in_blank_question)

    blank_space = 0


    while turns > 0 and blank_space < number_of_questions:
        current_blank = blank_index[blank_space]
        user_answer = input("Please fill in {}: ".format(current_blank))

        if user_answer == fill_in_blank_answer[blank_space]:
            print ("Correct! It is {}".format(user_answer))
            blank_space+=1
        else:
            print ("Incorrect. Please try again.\n")
            turns-=1
    else:
        outcome(blank_space)

def outcome(blank_space):
    if blank_space == number_of_questions:
        print ('Congratulations!!!')
        print(' You have successfully completed the quiz!')
    else:
        print ('You have run out of turns!')
        print('You completed {0} questions in {1} turn(s).'.format(blank_index,
            turns))
        continue_question()

def continue_question():
    continue_response = input("Would you like to continue (yes/no)?: ")
    if continue_response.lower() == 'yes':
        return complete_quiz()
    else:
        exit()

def complete_quiz():
   #Used to initialize the game.
    print ("Welcome to My Quiz!!!! \n")
    quiz_question(difficulty_level)

complete_quiz()
