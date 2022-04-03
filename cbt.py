import csv
import tkinter as tk

"""This is a Computer-Based Testing/Exam Program.
This program is made with in the context of an objective exam for a high school called National Secondary School."""


print("NATIONAL SECONDARY SCHOOL, AWKA")
print("2ND TERM EXAMINATION")
print("Class: SS1")
print("Time: 1hr")
print("Section A: Objectives")

filename = "question_bank.csv"
score = 0

name = input("\n\nEnter your Name: ")
reg_no = input("Enter your Registration Number: ")
start = input("Start Exam (y/n): ")

def main():
    students = create_student_account(name, reg_no, score)
    question_bank = read_quest_file(filename)
    question = print_question(question_bank)

    print(students)
    print(question)

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
        question_bank = csv.reader(question_bank)
        #Skip the first row.
        next(question_bank)
        for row in question_bank:
            quest = row[0]
            option_a = row[1]
            option_b = row[2]
            option_c = row[3]
            option_d = row[4]
            answer = row[5]
            bank.append({"question": quest, "option_a": option_a, "option_b": option_b,\
            "option_c": option_c, "option_d": option_d, "answer": answer})
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
        


if __name__ == "__main__":
    main()