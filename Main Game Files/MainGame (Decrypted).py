#ITE-260 Python Game Project
#Due Date: December 6
#PRE-ALPHA CODE
#v1.0.0
game_running = True

repeat_loop = input("Would You like to Play? Y/N: ").upper()
questions = (
             "What is the third planet from the Sun?: ",
             "When is Christmas Day?: ",
             "What is the Philippine National Tree: ",)

choices = [("A. Earth", "B. Jupiter", "C. Mars", "D. Venus"),
           ("A. November 1", "B. December 31", "C. December 24", "D. December 25"),
           ("A. Christmas Tree", "B. Mango Tree", "C. Narra Tree", "D. Coconut Tree")]

correct_answers = ("A", "D", "C")
player_answers = []
question_number = 0


while game_running:
    player_score = 0
    player_name = input("ENTER YOUR NAME: ").upper()
    print()
    print("--------------------------------------------")
    print("--------------------------------------------")
    print("WELCOME TO MIND MASTERS,", player_name)
    print("\nVersion 1.0.0\nPre-alpha Build\nMore Questions will be added on final release\nThis is a sample build")
    print("--------------------------------------------")
    print("--------------------------------------------")
    print()
    print("1. Start Game")
    print("2. Exit")
    print()
    player_option = int(input("Select an Option: "))
    print()
    if player_option == 1:
        print("--------------------------------------------")
        print("               GAME START                   ")
        print("--------------------------------------------")
        print()
        for question in questions:
            print()
            print(question)
            print()
            for choice in choices[question_number]:
                print(choice)
                print()
            input_answer = input("Enter (A, B, C, D): ").upper()
            player_answers.append(input_answer)
            print()
            if input_answer == correct_answers[question_number]:
                print()
                print(input_answer,"is Correct!")
                player_score += 5
                print("Your Score: ", player_score)
                print()
                print("--------------------------------------------")
            else:
                print(input_answer ," is Incorrect!")
                print("Your Score: ", player_score)
                print()
                print("--------------------------------------------")
            question_number += 1
    else:
        break
    repeat_loop = input("Would You Like to Play Again? (Y/N): ").upper()
    question_number = 0
    if repeat_loop == "N":
        game_running = False
