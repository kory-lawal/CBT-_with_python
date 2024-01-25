import mysql.connector
import os
import time

"""
Create a function that handles mysql connection termination.
"""
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "question_and_answer"
)

cursor = mydb.cursor()

# cursor.execute(f"CREATE DATABASE question_and_answer")
cursor.execute("""CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255)NOT NULL
)""")



class user:
    def __init__(self,param):
           self.param = param

    def welcome(self):
        if self.param == 1:
            self.login()
        elif self.param == 2:
            self.register()
        else:
            print('what are you doing?') 

    def login(self): 
        try:
            print("Signing In")
            username = input("username: ")
            password = input("password: ")
            

            query = 'SELECT * FROM users where username=%s and password=%s'
            value = (username,password)
            db_rows = cursor.execute(query,value)
            
            results = cursor.fetchall()
            mydb.commit()
            cursor.close()
            mydb.close()
           
            if results:
                print("Login successful!")
                play_game(questions)
                

            else:
                print("Login failed. please try again or register.")
                os.system('cls')
                self.welcome()
                # db_rows = cursor.execute(query,value)
                


               
        except Exception as e:
            self.welcome()


    def register(self):
        print("Creating A New Accunt")
        username = input("username: ")
        email = input("Email: ")
        password = input("password: ")
        confirmpassword = input("confirmpassword: ")
        print(confirmpassword)

        try:
            if password == confirmpassword:
                query = 'INSERT INTO users (username, email, password) VALUES (%s,%s,%s)'
                print(query)
                userDetails = (username, email, password)

                cursor.execute(query, userDetails)


                mydb.commit()
                cursor.close()
                mydb.close()

                print("Registration successful")
                self.start_game()
            else:
                self.register()
                os.system("cls")
        except Exception as e:
            print(e)

    def start_game(self):
        print("Welcome to the Question and Answer Game!")

        play_game(questions)




class Question:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

questions = [
    Question("What is the capital of France?", ["a) London", "b) Berlin", "c) Paris", "d) Madrid"], "c"),
    Question("Which planet is known as the Red Planet?", ["a) Mars", "b) Venus", "c) Jupiter", "d) Saturn"], "a"),
    Question("What is 2 + 2?", ["a) 3", "b) 4", "c) 5", "d) 6"], "b"),
]

def play_game(questions):
    score = 0
    incorrect_answers = []  # Store the indices of questions with incorrect answers

    for i, question in enumerate(questions, 1):
        print(f"Question {i}: {question.question}")
        for option in question.options:
            print(option)

        user_answer = input("Select the correct option (a/b/c/d):")
        if user_answer == question.answer:
            score += 1
        else:
            incorrect_answers.append(i - 1)

    print("\nGame Over! You scored", score, "out of", len(questions), "points.")

    if incorrect_answers:
        print("You got the following questions wrong:")
        for index in incorrect_answers:
            correct_answer = questions[index].answer
            print(f"Question {index + 1}: {questions[index].question} (Correct Answer: {correct_answer})")

if __name__ == "__main__":
    print("Welcome to the Question and Answer Game!")
    game = int(input("1.login\n2.signin\n"))
    init_class = user(game)
    init_class.welcome()
# play_game(questions)
