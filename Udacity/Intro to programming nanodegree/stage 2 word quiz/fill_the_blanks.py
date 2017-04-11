test_blanks = ["__1__","__2__","__3__","__4__"]

#The easy empty fill-in-the blank and its corresponding answers.
easy_quest = "A computer __1__ is a typewriter-style __2__ which uses an \
arrangement of __3__ or keys to act as a mechanical lever or electronic switch. \
Following the decline of punch cards and paper tape, interaction via \
teleprinter-style keyboards became the main input device for __4__."

easy_answer = ["keyboard", "device", "buttons", "computers"]

#The medium empty fill-in-the blank and its corresponding answers.
medium_quest = "A computer __1__ is a pointing device (hand control) that detects two-dimensional \
__2__ relative to a surface. This __2__ is typically translated into the __2__ \
of a pointer on a __3__, which allows a smooth control of the graphical user __4__."

medium_answer = ["mouse", "motion", "display", "interface"]

#The hard empty fill-in-the blank and its corresponding answers.
hard_quest = "A computer __1__ or a __3__ display is an electronic visual display \
for computers. A __1__ usually comprises the display device, __4__, casing, \
and power supply. The display device in modern monitors is typically \
a thin film __2__ liquid crystal display (TFT-LCD) or a flat panel LED display, \
while older monitors used a cathode ray tubes (CRT). It can be connected to the __3__ \
via VGA, DVI, HDMI, DisplayPort, Thunderbolt, LVDS (Low-voltage differential signaling) \
or other proprietary connectors and signals."

hard_answer = ["monitor", "transistor", "computer", "circuitry"]


def start_game():
    '''This function starts the game by printing the below statment.
    '''
    print "\n Welcome to the computer device word quiz !!\n"
    game_difficulty() #It starts game_difficulty function.

def game_difficulty():
    '''This function begins by printing the below statement. User can select easy
    or medium or hard. That is input value. If input is set, the output is the
    function check_answer and printing input value.
    '''
    level = raw_input("Please select a difficulty (easy, medium, hard): ")
    if level.lower() == "easy":
        return check_answer(easy_quest, easy_answer, test_blanks), "easy"
    if level.lower() == "medium":
        return check_answer(medium_quest, medium_answer, test_blanks), "medium"
    if level.lower() == "hard":
        return check_answer(hard_quest, hard_answer, test_blanks), "hard"
    else:
        print "You selected an invalid difficulty level!!"
        return game_difficulty() #If user select an invalid difficulty level, This function starts again.

def answer_replacer(select_quest, user_answer, location_count):
    '''This function replace blanks of select_quest to user_answers using location_count.
    '''
    replaced = [] #It will be appended list items (select_quest + answer)
    select_quest_list = select_quest.split() #this splits select_quest into a list
    for word in select_quest_list:
        replacement = test_blanks[location_count]
        if replacement != None:
            word = word.replace(replacement, user_answer)
            replaced.append(word)
        else:
            replaced.append(word)
    replaced = " ".join(replaced) #This returns a string, which is the concatenation of the strings.
    return replaced

def check_answer(select_quest, select_answer, test_blanks):
    '''This function check if the answer is correct or not. User can write user_answer.
    If user_answer is right, blank of select_quest will be replaced by user_answer through answer_replacer.
    '''
    location_count = 0
    while location_count < len(test_blanks):
        print select_quest + " \n"
        print "Please fill in blank #" + test_blanks[location_count]
        user_answer = raw_input("").lower() #It's okay even if user write in capitals.
        if user_answer == select_answer[location_count]:
            print "\n That is correct! It is " + select_answer[location_count] + "! \n"
            select_quest = answer_replacer(select_quest, user_answer, location_count) + '\n'
            location_count = location_count + 1
        else:
            print "\n That is incorrect! Try again. \n"
    return end()

def end():
    '''This function print below statement.
    '''
    print ("Congratulations, You have filled in all of the blanks! You are genious.")

start_game()
