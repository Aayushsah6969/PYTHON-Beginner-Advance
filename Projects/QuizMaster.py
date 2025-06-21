# Building a quiz game in Python. Question will be stored and fetched from a json file. Displayed in terminal. Time starts as question displays till users input an answer. after all questions done, result will be displayed.
#question file: {id:number, level:easy/medium/hard, question:string, answer:string, options:[string]}
#begining of game, user will input name and new file will be made in name of users to store the results. display results and delete the file.

import json  # For loading the JSON question bank
import time  # For timing each question
import random  # For shuffling questions/options
import os  # For file deletion

# === Quiz Setup ===
print("Welcome to Quizmaster...")

userName = input("To start the quiz, please enter your name: ")
userFile = open(f"{userName}.txt", "w")

userFile.write(f"UserName: {userName}\n")
userFile.write("totalScore: 0\n")

Qtype = input("Please select the type of quiz you want to play (easy/medium/hard): ").lower()
userFile.write(f"QuizType: {Qtype}\n")

Qnum = int(input("How many questions do you want to attempt? (1-10): "))
if Qnum < 1 or Qnum > 10:
    print("Please enter a number between 1 and 10.")
    exit()

userFile.write(f"Number of Questions: {Qnum}\n")

timeLimit = 30  # Time limit per question in seconds
total_time = 0  # Total time for all questions
score = 0  # Score counter

# === Load Questions ===
with open("questions.json", "r") as Qbank:
    questions = json.load(Qbank)

# Filter and prepare questions
filtered_questions = [q for q in questions if q["level"] == Qtype]
random.shuffle(filtered_questions)
selected_questions = filtered_questions[:Qnum]

# === Ask Question Function ===
def ask_question(question, number):
    print(f"\nQuestion {number}: {question['question']}")
    options = question['options']
    random.shuffle(options)

    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    start_time = time.time()

    try:
        answer_index = int(input("Enter the option number: "))
        user_answer = options[answer_index - 1]
    except (ValueError, IndexError):
        user_answer = None
        print("Invalid input! No answer recorded.")

    end_time = time.time()
    time_taken = round(end_time - start_time, 2)

    # Check time limit
    if time_taken > timeLimit:
        print(f"⏰ Time's up! You took {time_taken} seconds (limit was {timeLimit}s).")
        return 0, time_taken, user_answer, "Time Exceeded"

    if user_answer == question["answer"]:
        print("✅ Correct!")
        return 1, time_taken, user_answer, "Correct"
    else:
        print(f"❌ Wrong! The correct answer was: {question['answer']}")
        return 0, time_taken, user_answer, "Wrong"

# === Game Loop ===
for i, q in enumerate(selected_questions, 1):
    result_score, time_used, user_ans, result_text = ask_question(q, i)
    score += result_score
    total_time += time_used

    userFile.write(f"\nQ{i}: {q['question']}\n")
    userFile.write(f"Your Answer: {user_ans} | Correct Answer: {q['answer']} | Result: {result_text} | Time: {time_used}s\n")

# === Final Summary ===
userFile.write("\n--- Quiz Summary ---\n")
userFile.write(f"Final Score: {score}/{Qnum}\n")
userFile.write(f"Total Time Taken: {round(total_time, 2)} seconds\n")
userFile.close()

# Display results and delete file
print("\n=== Your Quiz Results ===")
with open(f"{userName}.txt", "r") as summary:
    print(summary.read())

os.remove(f"{userName}.txt")
