questions = ("What is the highest peak in the world?",
            "who is the prime minister of the country nepal?",
            "How many elements are there in periodic table?",
            "How many bones are there in human body",
            "Which is the hottest planet in the solar system?",
            "Who is the crush of narendra modi?")

options = (("A. Ambani ka ghar ","B. lodha building ","C. Mount everest ","D. K2 "),
           ("A. Dharmendra pradhan ","B.  arvind kejriwal ","C. Rahul gandhi","D. Balendra shah"),
           ("A. 206 ","B. 69 ","C. 67","D. 118"),
           ("A. 118 ","B. 207 in morning ","C. 7 crore ","D. 206 "),
           ("A. Earth", "B. Venus", "C. Mars", "D. Jupiter"),
           ("A. mamta banerji ","B. meloni ","C. kangana ranaut ","D. sunny deol "),)

answers = ("C", "D", "D", "D", "B", "B")

score = 0

for question_num, question in enumerate(questions):
    print("-------------------------")
    print(f"\nQuestion {question_num + 1} of {len(questions)}")
    print(question)

    for option in options[question_num]:
        print(option)

    while True:
        guess = input("Enter (A,B,C,D): ").strip().upper()

        if guess in ("A", "B", "C", "D"):
            break
        else:
            print("Invalid!! Please enter the valid option (A, B, C or D)")

    if guess == answers[question_num]:
        score += 1
        print("Correct")
    else:
        print("Incorrect")
        print(f"{answers[question_num]} is the correct answer")

print("------------------------------")
print("         FINAL RESULTS        ")
print("------------------------------")

total_questions = len(questions)
percentage = (score / total_questions) * 100

print(f"You got {score} out of {total_questions} correct!")
print(f"Your score percentage is: {percentage:.2f}%")

if percentage >= 80:
    print("Excellent work! 🎉")

elif percentage >= 60:
    print("Good job! Keep it up! 👍")

elif percentage >= 40:
    print("Keep practising! You're improving. 😊")

else:
    print("Don't give up! Practice makes progress. 💪")
