import tkinter as tk
import csv
from tkinter.font import BOLD

HEIGHT = 700
WIDTH = 800
filename = "question_bank.csv"



def read_quest_file(filename):

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
    questions_only = []
    for question in bank:
        quest = question[0]
        questions_only.append(quest)
    return questions_only

def retrieve_options(bank):
    for question in bank:
        option_a = question[1]
        option_b = question[2]
        option_c = question[3]
        option_d = question[4]
        return (f"{option_a} {option_b} {option_c} {option_d}")

def show_question():
    bank = read_quest_file(filename)
    questions = retrieve_questions(bank)
    
    for _ in range(0,11):
        questions = retrieve_questions(bank)
        lbl_quest.config(text=f"{questions[0]}\n{questions[1]}\n{questions[2]}\n{questions[3]}\n")

        
   
           



# Create root object.
root = tk.Tk()
# open window in max size.
root.state("zoomed")

frm_main = tk.Frame(root, bg="#a0ced9")
frm_main.place(relwidth=1, relheight=1)

# Create start button.
btn_start = tk.Button(frm_main, text="Click to start", font=("Comic Sans MS", 14, BOLD), fg="green", border=5, command=show_question)
btn_start.place(relx=0.5, rely=0.95, anchor="s", relwidth=0.15, relheight=0.05)

#create a label for the questions.
lbl_quest = tk.Label(frm_main, bg="white")
lbl_quest.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.8)

root.mainloop()


