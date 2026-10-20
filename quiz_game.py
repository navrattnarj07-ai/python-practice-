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
           ("A. my future wife ","B. earth ","C. Sun ","D. Moon"),
           ("A. mamta banerji ","B. meloni ","C. kangana ranaut ","D. sunny deol "),)

answers = ("C", "D", "D", "D", "C", "B" )
gueses = []
score = 0
question_num = 0 


for question in questions:
    print("-------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A,B,C,D): ").upper()
    gueses.append(guess)
    if guess == answers[question_num]:
        score+=1
        print("Correct")
    else:
        print("Incorrect")
        print(f"{answers[question_num]} is the correct answer")

    question_num +=1

print("-------------------------")
print("---------Results---------")
print("-------------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("gueses: ", end="")
for guess in gueses:
    print(guess, end=" ")
print()

