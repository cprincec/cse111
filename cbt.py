import csv
import tkinter as tk

"""This is a Computer-Based Testing/Exam Program.
This program is made with in the context of an objective exam for a high school called National Secondary School."""


print("NATIONAL SECONDARY SCHOOL, AWKA")
print("2ND TERM EXAMINATION")
print("Class: SS1")
print("Time: 1hr")
print("Section A: Objectives")

def main():
    #Create the tk root object.
    root = tk.Tk()
    #Create the main window.
    frm_main = tk.Frame(root, bg="blue")
    frm_main.master.title("COMPUTER BASED EXAMINATION PROGRAM")
    frm_main.pack()

    root.mainloop()

    # filename = "question_bank.csv"
    # score = 0
    # choices = ["a", "b", "c", "d"]
    # name = input("\n\nEnter your Name: ")
    # reg_no = input("Enter your Registration Number: ")
    # start = input("Start Exam (y/n): ")

    # students = create_student_account(name, reg_no, score)
    # question_bank = read_quest_file(filename)
    
    # for question in question_bank:

    #     quest =  question["question"]
    #     a = question["option_a"]
    #     b = question["option_b"]            
    #     c = question["option_c"]
    #     d = question["option_d"]
    #     answer = question["answer"]

    #     print(f"{quest} \n\nA. {a} \nB. {b} \nC. {c} \nD. {d}")

    #     choice =  input(">>> ") 
    #     while choice.lower() not in choices:
    #         print("Invalid option.") 
    #         print("Enter A or B or C or D.")
    #         choice =  input(">>> ")      
    #     if choice == answer:
    #         score += 1
    #     else:
    #         pass
    # print(f"{name}, You scored {score} out of 11.") 
              

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

def print_question(question_bank):
    """Print 10 questions one at a time from a question bank 
    
    Parameters:
        question_bank: dictionary of objective questions and options.
    Return: nothing
    """
    question_num = 1
    #Loop through the question bank and print 10 questions
    #with heading of question 1, question 2 and so on.
    
        
    for question in question_bank: 
        print(question)
        




if __name__ == "__main__":
    main()