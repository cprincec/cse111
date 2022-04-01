import tkinter as tk
import csv
from tkinter.font import BOLD

HEIGHT = 700
WIDTH = 800
filename = "question_bank.csv"
info = ("NATIONAL SECONDARY SCHOOL, AWKA\n\n2ND TERM EXAMINATION\n\nClass: SS1\n\nTime: 1hr\n\nSection A: Objectives")


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

def show_question(frm_main):
    bank = read_quest_file(filename)
    questions = retrieve_questions(bank)
    
    for _ in range(0,10):
        questions = retrieve_questions(bank)
    frm_heading = tk.Frame(frm_main, bg="orange")
    frm_heading.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.07)
    lbl_heading = tk.Label(frm_heading, text="Subject: Data Processing    |   Class: SS1   |    Time: 1hour", bg= "orange", fg="white", font="Arial 22 bold")
    lbl_heading.place(relx=0.15, rely=0.3)
    lbl_quest.config(text=f"1. {questions[0]}\n\n2. {questions[1]}\n\n3. {questions[2]}\n\n4. {questions[3]}\n\n5. {questions[4]}\n\n6. {questions[5]}\n\n7. {questions[6]}\n\n8. {questions[7]}\n\n9. {questions[8]}\n\n10. {questions[9]}\n\n", justify="left", font=("Arial", "16"))
    lbl_quest.place(relx=0.05, rely=0.08, relwidth=0.9, relheight=0.9)
    btn_start.destroy()
        


# Create root object.
root = tk.Tk()
# open window in max size.
root.state("zoomed")

frm_main = tk.Frame(root, bg="#a0ced9")
frm_main.place(relwidth=1, relheight=1)


# Create start button.
btn_start = tk.Button(frm_main, text="Click to start", font=("Comic Sans MS", 14, BOLD), fg="green", border=5, command=lambda: show_question(frm_main))
btn_start.place(relx=0.5, rely=0.95, anchor="s", relwidth=0.15, relheight=0.05)

#create a label for the questions.
lbl_quest = tk.Label(frm_main, text=info, bg="white", font=("Arial", "20", "bold"))
lbl_quest.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.8)

root.mainloop()


