score = 0
total = 5

questions = {

    "What is the largest ocean on Earth?\n"
    "  a) Atlantic Ocean\n  b) Indian Ocean\n  c) Arctic Ocean\n  d) Pacific Ocean\n"
    "Type a/b/c/d: ": "d",

    "What is the best day of the week?\n"
    "  a) Monday\n  b) Wednesday\n  c) Thursday\n  d) Saturday\n"
    "Type a/b/c/d: ": "d",

    "In computing, what does 'CPU' stand for?\n"
    "  a) Central Process Unit\n  b) Central Processing Unit\n  c) Computer Processing Utility\n  d) Core Processing Unit\n"
    "Type a/b/c/d: ": "b",

    "True or False: The chemical symbol for gold is Au.\n"
    "Type True/False: ": "true",

    "True or False: Leonardo da Vinci Painted the Mona Lisa.\n"
    "Type True/False: ": "true",
}

print("Welcome to Quiz Bowl! Answer the questions below.\n")

for prompt, correct in questions.items():
    user = input(prompt)
    if user == correct:
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect. The correct answer is: ", correct)

print("\nYour score: ",score," out of ",total)
