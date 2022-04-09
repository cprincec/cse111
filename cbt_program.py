import tkinter as tk
import csv
from tkinter.font import BOLD


"""Welcome to the Computer Based Exam program. This program will enable teachers to administer exams to students using computers. 
To use this program, the question bank needs to be updated with the necessary questions, options and correct answer to each question.

To start the exam, the student clicks the start button.
To submit the exam, the students clicks the submit button."""


# This variable keeps track of the current question displayed on the screen
CURRENT = 0

# This keeps track of the students score.
SCORE = 0

# The question bank file.
filename = "question_bank.csv"

# The exam info to be displayed on the first frame/screen.
info = ("NATIONAL SECONDARY SCHOOL, AWKA\n\n2ND TERM EXAMINATION\n\nClass: SS1\n\nTime: 1hr\n\nSection A: Objectives")

def main():

    # Create root object.
    root = tk.Tk()
    # open root window in max size.
    root.state("zoomed")

    # create the main frame
    frm_main = tk.Frame(root, bg="#a0ced9")
    frm_main.place(relwidth=1, relheight=1)

    # Create start button.
    # To be click inorder to start the exam.
    btn_start = tk.Button(frm_main, text="Click to start", font=("Comic Sans MS", 14, BOLD), fg="green", border=5, command=lambda: show_question(frm_main, frm_lbl_quest, btn_start, lbl_quest))
    btn_start.place(relx=0.5, rely=0.95, anchor="s", relwidth=0.15, relheight=0.05)

    # create a frame for questions label.
    frm_lbl_quest = tk.Frame(frm_main, bg="white")
    frm_lbl_quest.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.8)

    #create a label for the questions.
    lbl_quest = tk.Label(frm_lbl_quest, text=info, bg="white", font=("Arial", "20", "bold"))
    lbl_quest.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.8)

    root.mainloop()



def read_quest_file(filename):
    """This function produces a question bank in the form of a compound list, from the csv file where questions are stored.

    Parameters:
        filename: csv file containing questions, options and answer.
    Return: 
        bank: compound list containing questions, options and corresponding answer.
    """
    bank = []
    with open(filename, "rt") as question_bank:
        reader = csv.reader(question_bank)
        next(reader)
        for row in reader:
            quest = row[0]
            option_a = row[1]
            option_b = row[2]
            option_c = row[3]
            option_d = row[4]
            answer = row[5]
            bank.append([quest,option_a,option_b,option_c,option_d,answer])
    return bank


def retrieve_questions(bank):
    """Retrieve only the questions from the questions bank and add them to a list.
    
    Parameter:
        bank: compound list containing questions, options and corresponding answer.
    Return: 
        questions_only: list containing only questions.
    """
    questions_only = []
    for question in bank:
        quest = question[0]
        questions_only.append(quest)
    return questions_only



def retrieve_options(bank):
    """Retrieve only the options from the questions bank and add them to a list.
    
    Parameter:
        bank: compound list containing questions, options and corresponding answer.
    Return: 
        options_only: list containing only options for each questions."""
    options_only = []
    for question in bank:
        option_a = question[1]
        option_b = question[2]
        option_c = question[3]
        option_d = question[4]
        options_only.append([option_a, option_b, option_c, option_d])
    return options_only


def retrieve_answers(bank):
    """Retrieve only the answers from the questions bank and add them to a list.
    Parameter:
        bank: compound list containing questions, options and corresponding answer.
    Return: 
        answers_only: list containing only questions.
    """
    answers_only = []
    for question in bank:
        answer = question[5]
        answers_only.append(answer)
    return answers_only


def show_question(frm_main, frm_lbl_quest, btn_start, lbl_quest):
    """This function will create widgets for page heading, question label and navigation buttons as well as display questions and
    corresponding options on the screen.
    
    Parameters:
        frm_main: The main frame.
        frm_lbl_quest: Frame for question label.
        btn_start: The start button.
        lbl_quest: Question label.
    Return: Nothing
    """
    global SCORE
    # Generate question, options and answer compound list.
    bank = read_quest_file(filename)
    # Generate question list.
    questions = retrieve_questions(bank)
    # Generate options list.
    options = retrieve_options(bank)
  
    
    # create a frame for heading label displaying the exam info.
    frm_heading = tk.Frame(frm_main, bg="orange")
    frm_heading.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.07)

    # create the heading label displaying the exam info.
    lbl_heading = tk.Label(frm_heading, text="Subject: Data Processing    |   Class: SS1   |    Time: 1hour", bg= "orange", fg="black", font="Arial 22 bold")
    lbl_heading.place(relx=0.15, rely=0.3)
    
    # Display question from question bank.
    lbl_quests = tk.Label(frm_lbl_quest, text=f"{questions[CURRENT]}", justify="left", font=("Arial", "18"), bg="white")
    lbl_quests.place(relx=0.01, rely=0.3, relwidth=0.9, relheight=0.3)
    
    # Create radio buttons for options to each question.
    # Each button triggers the compute_score function that will determine if the selected option is correct.
    menu = tk.StringVar()
    menu.set(menu)
    space = 0.5
   
    optiona_button = tk.Radiobutton(frm_lbl_quest, text=options[CURRENT][0], variable=menu, bg="white", value=options[CURRENT][0], anchor="w", font="Arial 13")   
    optiona_button.place(relx=0.15, rely=space, relwidth=0.6, relheight=0.03)
    space += 0.05
    optionb_button = tk.Radiobutton(frm_lbl_quest, text=options[CURRENT][1], variable=menu, bg="white", value=options[CURRENT][1], anchor="w", font="Arial 13")   
    optionb_button.place(relx=0.15, rely=space, relwidth=0.6, relheight=0.03)
    space += 0.05
    optionc_button = tk.Radiobutton(frm_lbl_quest, text=options[CURRENT][2], variable=menu, bg="white", value=options[CURRENT][2], anchor="w", font="Arial 13")   
    optionc_button.place(relx=0.15, rely=space, relwidth=0.6, relheight=0.03)
    space += 0.05
    optiond_button = tk.Radiobutton(frm_lbl_quest, text=options[CURRENT][3], variable=menu, bg="white", value=options[CURRENT][3], anchor="w", font="Arial 13")   
    optiond_button.place(relx=0.15, rely=space, relwidth=0.6, relheight=0.03)

    # Create next button.
    # Triggers the show_next function.
    btn_next = tk.Button(frm_main, text="Next", font=("Comic Sans MS", 15, BOLD), bg="orange", fg="black", command= lambda: [show_next_question(btn_next, btn_submit, lbl_quests, optiona_button,  optionb_button, optionc_button, optiond_button), compute_score(menu.get())])
    btn_next.place(relx=0.7, rely=0.95, anchor="s", relwidth=0.1, relheight=0.05) 

    # Create back button.
    # Triggers the show_previous function.
    btn_back = tk.Button(frm_main, text="Back", font=("Comic Sans MS", 15, BOLD), bg= "orange", fg="black", command=lambda: show_previous_question(btn_submit, btn_next, lbl_quests, optiona_button,  optionb_button, optionc_button, optiond_button))
    btn_back.place(relx=0.3, rely=0.95, anchor="s", relwidth=0.1, relheight=0.05) 

    # Button to enable submission.
    # This button will be placed on the screen only when the user gets to the last question
    btn_submit = tk.Button(frm_main, text="Submit", font=("Comic Sans MS", 15, BOLD), bg="black", fg="white", border=2, command= lambda: [compute_score(menu.get()), show_score(frm_heading, lbl_quests, btn_next, btn_back, optiona_button,  optionb_button, optionc_button, optiond_button, btn_submit)])

    
    # Remove/wipe the "Click to start" button from the screen so that the questions
    # can be displayed on the screen.
    btn_start.destroy()
    lbl_quest.destroy()
    

   
        


    def show_next_question(btn_next, btn_submit, lbl_quests, optiona_button,  optionb_button, optionc_button, optiond_button):
        """This function displays the next question in the question bank and its corresponding options."""
        
        global CURRENT
        bank = read_quest_file(filename)
        questions = retrieve_questions(bank)
        options = retrieve_options(bank)

        # increase current question tracker index.
        CURRENT += 1
        
        # Display question next from question bank.
        lbl_quests.config(text=f"{questions[CURRENT]}", justify="left", font=("Arial", "18"))

        # modify the options labels to correspond with the current question on the screen.        
        optiona_button.config(text=options[CURRENT][0], value=options[CURRENT][0])   
        optionb_button.config(text=options[CURRENT][1], value=options[CURRENT][1])
        optionc_button.config(text=options[CURRENT][2], value=options[CURRENT][2])
        optiond_button.config(text=options[CURRENT][3], value=options[CURRENT][3])

        # Replace the NEXT button with the SUBMIT button when the user gets to the last question.
        if CURRENT == 10:
            # Remove the 'Next' button.
            btn_next.place_forget()
            
            # Place the submit button.
            btn_submit.place(relx=0.7, rely=0.95, anchor="s", relwidth=0.1, relheight=0.05)
            

    def show_previous_question(btn_submit, btn_next, lbl_quests, optiona_button,  optionb_button, optionc_button, optiond_button):
        """This function displays the previous question in the question bank and its corresponding options."""
        global CURRENT
        bank = read_quest_file(filename)
        questions = retrieve_questions(bank)
        options = retrieve_options(bank)


        # this will screen displays the first question when the user clicks the PREVIOUS button
        # while on the first question.
        if CURRENT < 0:
            show_question(frm_main)     
        
        elif CURRENT > 0 and CURRENT <= 10:
            CURRENT -= 1
            
            # Display previous question from question bank.
            lbl_quests.config(text=f"{questions[CURRENT]}", justify="left", font=("Arial", "18"))
            
            # modify the options labels to correspond with the current question on the screen.
            optiona_button.config(text=options[CURRENT][0], value=options[CURRENT][0])   
            optionb_button.config(text=options[CURRENT][1], value=options[CURRENT][1])
            optionc_button.config(text=options[CURRENT][2], value=options[CURRENT][2])
            optiond_button.config(text=options[CURRENT][3], value=options[CURRENT][3]) 
            
            # Replace the SUBMIT button with the NEXT button when the user clicks PREVIOUS while on the last question.
            btn_submit.place_forget()
            btn_next.place(relx=0.7, rely=0.95, anchor="s", relwidth=0.1, relheight=0.05)
            


    def show_score(frm_heading, lbl_quests, btn_next, btn_back, optiona_button,  optionb_button, optionc_button, optiond_button, btn_submit):
        """This function will Clear all questions and buttons from the screen and display the user's total score"""
        global SCORE
        # delete all buttons and headings.
        optiona_button.destroy()
        optionb_button.destroy()
        optionc_button.destroy()
        optiond_button.destroy()
        frm_heading.destroy()
        btn_next.destroy()
        btn_back.destroy()
        btn_submit.destroy()
        
        # Display Exam score on the screen.
        lbl_quests.config(text=f"You have Successfully Submitted the exam.\n\n\n\n\n\n Your Total Score is {SCORE} out of 10", font="times 18 bold", justify= "center")

        
    def compute_score(user_answer):
        """Calculate the users score given each option selected per question.
        
        Parameter:
            User_answer: value of option selected using the radio buttons per question
        Return: Score.
        """
        global CURRENT
        global SCORE
        bank = read_quest_file(filename)
        answers = retrieve_answers(bank)
        
        if user_answer == (answers[CURRENT-1]):
            SCORE += 1
            
        return SCORE


if __name__ == "__main__":
    main()



