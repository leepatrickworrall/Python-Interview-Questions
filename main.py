import random


def select_random_question():
    with open("questions.txt", "r", encoding="utf-8") as file:
        questions = file.readlines()
    return random.choice(questions).strip()


def question_amount_choice():
    while True:
        try:
            question_amount = int(input("How many questions would you like?\n"))

            if question_amount > 0:
                return question_amount

            else:
                print("Please enter a positive number.")

        except ValueError:
            print("Please enter a valid number.")


def main():
    while True:
        question_amount = question_amount_choice()

        for _ in range(question_amount):
            question = select_random_question()
            print("Question:", question)

        more_questions = input("\nWould you like to view more questions? "
                               "(Yes/No)\n")

        if more_questions.lower() != "yes":
            break


if __name__ == "__main__":
    print("\nPython Interview Questions\n")
    main()