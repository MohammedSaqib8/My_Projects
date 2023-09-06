# ------------------------------------------
def new_game():
    guesses = []
    correct_guesses = 0
    question_number = 1

    for key in questions:
        print("--------------------------------------------")
        print(key)
        for i in options[question_number - 1]:
            print(i)

        guess = input("Enter (A,B,C,or D): ").upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_number += 1

    show_score(correct_guesses, guesses)


# ------------------------------------------
def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    elif answer != guess:
        print("WRONG!")
        return 0


# ------------------------------------------
def show_score(correct_guesses, guesses):
    print("--------------------------------------------")
    print("RESULTS:")
    print("--------------------------------------------")

    print("ANSWERS: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("GUESSES: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int(correct_guesses/len(questions) * 100)
    print("Your score is " + str(score) + "%")

    if score == 100:
        print("YOU ROCK!")
    elif 100 > score >= 50:
        print("GOOD!")
    elif 50 > score > 0:
        print("AVERAGE")
    elif score == 0:
        print("AW BUMMER! TRY AGAIN.")


# ------------------------------------------
def play_again():
    response = input("Do you want to play again? (yes/no): ").lower()
    if response == "yes":
        return True
    else:
        return False


# ------------------------------------------

questions = {
    "Who is considered as Father of Sociology?: ": "C",
    "The term sociology is derived from Latin word 'Socius' and 'logos', which means....: ": "D",
    "Influence of French Revolution (year?): ": "B",
    "Which is NOT a characteristic of Sociology?: ": "C",
    "Who wrote the book 'The Origin of the Species'?: ": "A"}

options = [
    ["A. Herbert Spencer", "B. Emile Durkheim", "C. Auguste Comte", "D. Karl Marx"],
    ["A. Standards and Logos", "B. Society and Origin", "C. Social and Status", "D. Companion and Study"],
    ["A. 1866", "B. 1789", "C. 1947", "D. 1777"],
    ["A. General Social Science", "B. Abstract Science", "C. Dependent Science", "D. Categorical"],
    ["A. Charles Darwin", "B. William Shakespeare", "C. Tolstoy", "D. P.B. Shelly"]]


new_game()
while play_again():
    new_game()

print("BYEEE")
