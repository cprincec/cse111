import tkinter as tk
import csv




"""Computer Based program designed with python"""


def show_frame(frame):
    frame.tkraise()

def main():

    filename = "question_bank.csv"
    score = 0
    choices = ["a", "b", "c", "d"]

    

    # create root object.
    root = tk.Tk()

    # open root object in maxsize.
    root.state("zoomed")
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)
    frm_main = tk.Frame(root)
    frm_questions = tk.Frame(root, bg="blue")

    # set title of main frame.
    frm_main.master.title("CBT Program")


    # place the main frame on the root object.
    for frame in (frm_main, frm_questions):
        frame.grid(row=0, column=0, sticky="nsew")

    show_frame(frm_main)
    populate_frames(frm_main, frm_questions)


    name = input("\n\nEnter your Name: ")
    reg_no = input("Enter your Registration Number: ")
    start = input("Start Exam (y/n): ")
    students = create_student_account(name, reg_no, score)
    question_bank = read_quest_file(filename)


    root.mainloop()


def create_student_account(name, reg_no, score):
    """Create a dictionary that stores a student's name, score with reg number as the key.

    Parameters:
        name: name of a student.
        reg_no: registration number of the student.
        score: total score of the students.
    return: compound list.
    """
    students = {}
    students[reg_no] = [name, score]
    return students

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
            bank.append({"question": quest, "option_a": option_a, "option_b": option_b, "option_c": option_c, "option_d": option_d, "answer": answer})
    return bank

def print_question(question_bank, choices, score):
        """Print 10 questions one at a time from a question bank 
        
        Parameters:
            question_bank: dictionary of objective questions and options.
        Return: nothing
        """
        question_num = 1
        #Loop through the question bank and print 10 questions
        #with heading of question 1, question 2 and so on.
        
        for question in question_bank:

            quest =  question["question"]
            a = question["option_a"]
            b = question["option_b"]            
            c = question["option_c"]
            d = question["option_d"]
            answer = question["answer"]

            print(f"{quest} \n\nA. {a} \nB. {b} \nC. {c} \nD. {d}")

            choice =  input(">>> ") 
            while choice.lower() not in choices:
                print("Invalid option.") 
                print("Enter A or B or C or D.")
                choice =  input(">>> ")      
            if choice == answer:
                score += 1
            else:
                pass    


def populate_frames(frm_main, frm_questions, question_bank, choices, score):
    """Display contents of the two pages on the window."""

    # information about the exam.
    info = ("NATIONAL SECONDARY SCHOOL, AWKA\n\n2ND TERM EXAMINATION\n\nClass: SS1\n\nTime: 1hr\n\nSection A: Objectives")

    # Create a label that displays the school information on start screen.
    lbl_info = tk.Label(frm_main, text=info, font= ("Heveltica", 40, "bold"), fg="blue")

    # create a button to be clicked
    # when ready to begin the exam.
    btn_begin = tk.Button(frm_main, text= "Begin Exam", bg= "blue", fg="white", 
                width=20, font= ("Heveltica", 20, "bold"), command=lambda: show_frame(frm_questions), command=print_question(question_bank, choices, score))

    lbl_info.pack(pady=150)
    btn_begin.pack()

    

if __name__ == "__main__":
    main()