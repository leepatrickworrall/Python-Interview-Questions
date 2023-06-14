import random


def select_random_question():
    with open("questions.txt", "r") as file:
        questions = file.readlines()
    return random.choice(questions).strip()


def question_amount_choice():
    while True:
        try:
            question_amount = int(input("How many questions would you like? "))

            if question_amount > 0:
                return question_amount

            else:
                print("Please enter a positive number.")

        except ValueError:
            print("Please enter a valid number.")


def main():
    while True:
        question_amount = question_amount_choice()
        print()

        for _ in range(question_amount):
            question = select_random_question()
            print("Question:", question)

        more_questions = input("\nWould you like to view more questions? "
                               "(Yes/No)\n")
        print()

        if more_questions.lower() != "yes":
            break


if __name__ == "__main__":
    print("\nPython Interview Questions\n")
    main()