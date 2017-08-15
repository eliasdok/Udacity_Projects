#Udacity Project

print "\nHello! Lets play a Quiz\n" + "You can choose the difficulty level: easy  medium or hard.\n"

#this is the list of blanks.
blanks = ["___1___","___2___","___3___","___4___"]

#all paragraphs have 4 main blanks. ask for user input to fill in the blanks . maximum  user guesses = 5.

#These are the strings for 3 levels.
questions_easy = ''' ___1___ invents the phone. ___2___ invents the elecricity.
___3___ invents radio communication. ___4___ invests car.'''

questions_medium = ''' ___1___ is the god of war, one of the Twelve Olympian gods and the son of Zeus and Hera. ___2___ is the king of the Greek Gods.
___3___ is the goddess of women and marriage in Greek mythology and religion. ___4___ was the goddess of love, sex, beauty, and fertility.'''


questions_hard = '''The web browser of Microsoft is  ___1___.  ___2___ is  Microsoft's founder.
The most populated country in the world is  ___3___ with 1,379,302 people.The most populated city in the workd is   ___4___ with 37,833,000 population.'''



#These are the individual lists for correct answers. We compare user input answer to these following lists.
answers_list_easy = ["Edisson", "Tesla", "Marconi", "Benz"]
answers_list_medium = ["Aris", "Zeus", "Hra", "Venus"]
answers_list_hard = ["Internet explorer", "Bill Gates", "China", "Tokyo"]


#this is the list of the difficulty levels
user_level_list = ["easy", "medium","hard"]

user_level = raw_input("Type in your difficulty level: ").lower()

#This function takes in the input string from user for the difficulty level and returns corresponding list as output.
def difficulty_level(user_level):
    '''
    Takes in user input for the level and gives the corresponding string or paragraphs.
    '''

    if user_level not in user_level_list:
        print "Not a valid option. Please enter a valid option (easy or medium)."
    else:
        if user_level == "easy":
            return questions_easy
        elif user_level == "medium":
            return questions_medium
        elif user_level == "hard":
            return questions_hard
        pass

#print difficulty_level(user_level)

#This function takes difficulty level string as input and returns corresponding list of answers for that level.
def relate_answer(user_level):
    '''
    Takes in user input for level and gives the corresponding list of answers.
    '''
    if difficulty_level(user_level) == questions_easy:
        return answers_list_easy
    if difficulty_level(user_level) == questions_medium:
        return answers_list_medium
    if difficulty_level(user_level) == questions_hard:
        return answers_list_hard
    pass

#print relate_answer(user_level)

#This function has inputs for the given answers by user, the correct answers from our corresponding list and the index in that list.
#gives output right or wrong depending on the answers.
def check_answer(user_answer, answers_list, answers_index):
    '''validate user answers with our correct answers list.'''

    if user_answer == answers_list[answers_index]:
        return "Correct"
    return "Wrong"
    pass

#print check_answer(user_answer,another_variable,answers)

#This is our play function which doesn't take any inputs. It calls the other functions and uses their input-output to give the results.
def play():
    '''This is the main function which allows to play the quiz.'''
    quiz = difficulty_level(user_level)         #gives the correct paragraph according to user input.
    print "\n" + quiz + "\nYou will get maximum 5 guesses for each blank.\n"
    answers_list = relate_answer(user_level)    #ensures we work in the proper list of answers.
    blanks_index,answers_index,number_of_guesses,guesses_limit= 0,0,5,0  #initialize variables so it doesn't give error later on/#initialize variables so it avoids magic numbers.                         

    while blanks_index < len(blanks):   #This loop executes so long as number of blanks are not replaced.
        user_answer = raw_input("type in your answer for " + blanks[blanks_index] + ": ")
        if check_answer(user_answer,answers_list,answers_index) == "Correct":
            print "Correct! that is the right answer!\n"
            quiz = quiz. replace(blanks[blanks_index],user_answer)
            blanks_index+=1
            answers_index+=1
            number_of_guesses =5
            print quiz
            if blanks_index == len(blanks):
                print "Congratulations! You win!"
        else:
            number_of_guesses -= 1
            if number_of_guesses == guesses_limit:
                print "Game over!"
                break
            else:
                print "please try again." + "You have " + str(number_of_guesses) + " guesses left."
    

play()
