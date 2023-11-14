import random
import time
game_running = True
questions =  [
    {
        'question': "What is the third planet from the Sun?:\n \nA. Earth\nB. Jupiter\nC. Mars\nD. Yekok\n ",
        'answer': "A"
    },
    {
        'question': "When is Christmas Day?:\n \nA. December 31\nB. Novermber 1\nC. December 25\nD. December 24\n ",
        'answer': "C"
    },
    {
        'question': "What is the Philippine National Tree?:\n \nA. Mango\nB. Christmas Tree\nC. Narra\nD. Coconut Tree\n ",
        'answer': "C"
    },
    {
        'question': "Optics is the study of what?:\n \nA. Eyes\nB. Light\nC. Space\nD. Opinions\n ",
        'answer': "B"
    },
    {
        'question': "What is the hardest natural substance on Earth?:\n \nA. Rock\nB. Titatnium\nC. Aluminum\nD. Diamond\n ",
        'answer': "D"
    },
    {
        'question': "How did Spider-Man get his powers?:\n \nA. He got bit by a Spider\nB. He was born with them\nC. He ate a Spider\nD. He bought his powers\n ",
        'answer': "A"
    },
    {
        'question': "What is the largest internal organ in the human body?:\n \nA. Lungs\nB. Heart\nC. Kidneys\nD. Liver\n ",
        'answer': "D"
    },
    {
        'question': "What is the percentage of the Earth covered by water?:\n \nA. 51%\nB. 61%\nC. 71%\nD. 81%\n ",
        'answer': "C"
    },
    {
        'question': "Which of the following is not a Japanese dish?:\n \nA. Sushi\nB. Ramen\nC. Babi guling\nD. Udon\n ",
        'answer': "C"
    },
    {
        'question': "What is the atomic number of Hydrogen?:\n \nA. 1\nB. 2\nC. 3\nD. 4\n ",
        'answer': "A"
    },
    {
        'question': "What shape is the constellation Ursa Major known to have?:\n \nA. A bear\nB. A ladle\nC. A circle\nD. A lion\n ",
        'answer': "A"
    },
    {
        'question': "What is the capital of the Philippines?:\n \nA. Cagayan De Oro\nB. Makati\nC. Wao\nD. Metro Manila\n ",
        'answer': "D"
    },
    {
        'question': "In which continent can the Philippines be found?:\n \nA. Australia\nB. Europe\nC. Asia\nD. South America\n ",
        'answer': "C"
    },
    {
        'question': "The Philippines was a colony for almost 400 years of which European country?:\n \nA. USA\nB. Japan\nC. Russia\nD. Spain\n ",
        'answer': "D"
    },
    {
        'question': "What is the name of the world-famous resort island located in the Visayan province of Aklan known for its white-sand beaches and vibrant nightlife?:\n \nA. Boracay\nB. Siargao\nC. Palawan\nD. Bali\n ",
        'answer': "A"
    },
    {
        'question': "Who is the current President of the Philippines who was elected earlier this year 2022?:\n \nA. Rodrigo Duterte\nB. Leni Robredo\nC. Ferdinand Marcos Jr.\nD. Ferdinand Marcos III\n ",
        'answer': "C"
    },
    {
        'question': "Which famous Portuguese explorer was killed in the Philippines while trying to circumnavigate the world?:\n \nA. Lapu-Lapu\nB. Ferdinand Magellan\nC. Cristiano Ronaldo\nD. Donald Trump\n ",
        'answer': "B"
    },
    {
        'question': "Which of these colours cannot be found in the Philippine flag?:\n \nA. White\nB. Green\nC. Yellow\nD. Blue\n ",
        'answer': "B"
    },
    {
        'question': "How many islands are there in the Philippine Archipelago?:\n \nA. 7,107\nB. 9,009\nC. 12,012\nD. 15,674\n ",
        'answer': "A"
    },
    {
        'question': "Which of these is the staple food of the Filipinos and is eaten at every meal?:\n \nA. Corn\nB. Bread\nC. Rice\nD. Adobo\n ",
        'answer': "C"
    },
    {
        'question': "Which of these is the informal term that Filipinos use to call themselves?:\n \nA. Pitoy\nB. Tisoy\nC. Panot\nD. Pinoy\n ",
        'answer': "D"
    },
    {
        'question': "What is the nickname of the Philippine International Football team?:\n \nA. Azkals\nB. PusaKals\nC. PhilippinesFC\nD. Sipa Pilipinas\n ",
        'answer': "A"
    },
    {
        'question': "What is the most popular and most played sport in the Philippines?:\n \nA. Dota 2\nB. Basketball\nC. Football\nD. Badminton\n ",
        'answer': "B"
    },
    {
        'question': "Who was the first Filipino President?:\n \nA. Gloria Arroyo\nB. Ninoy Aquino\nC. Emilio Aguinaldo\nD. Ellie Soriano\n ",
        'answer': "C"
    },
    {
        'question': "What is the name of the common Filipino dish that is marinated in soy sauce, vinegar, garlic, and pepper?:\n \nA. Adobo\nB. Sinigang\nC. Pakbet\nD. Lauya\n ",
        'answer': "A"
    },
    {
        'question': "What is the largest island in the Philippines?:\n \nA. Visayas\nB. Luzon\nC. Palawan\nD. Samal\n ",
        'answer': "B"
    },
    {
        'question': "Biology is the study of what?:\n \nA. Atmosphere\nB. Rocks\nC. Living Things\nD. Money\n ",
        'answer': "C"
    },
    {
        'question': "A species with no living members has become what?:\n \nA. Alive\nB. Numerous\nC. Extinct\nD. Legendary\n ",
        'answer': "C"
    },
    {
        'question': "Which biologist first put forward the theory of evolution?:\n \nA. Apollo Quiboloy\nB. Charles Darwin\nC. Charles Xavier\nD. Charlie Chaplin\n ",
        'answer': "B"
    },
    {
        'question': "Which one of these terms describes the lowest member of the food chain?:\n \nA. Producer\nB. Herbivore\nC. Primary\nD. Digester\n ",
        'answer': "A"
    },
    {
        'question': "Ornithology is the study of what?:\n \nA. Fish\nB. Birds\nC. Reptile\nD. Amphibians\n ",
        'answer': "C"
    },

]

random.shuffle(questions)

while game_running:
    player_life = 3
    player_score = 0
    score_limit = 100
    print()
    player_name = input("Enter Your Name: ")
    print()
    print("--------------------------------------------")
    print("--------------------------------------------")
    print("WELCOME TO MIND MASTERS,", player_name)
    print("Version 1.0.0\nPre-alpha Build\nMore Questions will be added on final release\nThis is a sample build")
    print("--------------------------------------------")
    print("--------------------------------------------")
    print()
    print("Please Select an Option (1/2): ")
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
            question_text = question.get("question")
            print(question_text)
            print()
            user_answer = input("Enter (A, B, C, D): ").upper()
            print()
            correct_answer = question.get("answer")
            if user_answer == correct_answer:
                print("Your answer is correct!")
                player_score += 5
                print(player_name + ", your Score is:", player_score)
                print("Lives Left: ",player_life)
                print()
                print("--------------------------------------------")
                print()
            else:
                print(user_answer,"is Incorrect!")
                print("The correct answer is,", correct_answer)
                print(player_name +", your Score is:", player_score)
                player_life -= 1
                print("Lives Left: ",player_life)
                print()
                print("--------------------------------------------")
                print()
            time.sleep(1)
            if player_life == 0:
                print("Game Over! No lives left!")
                print()
                break
            if player_score == score_limit:
                print("----------------------------")
                print("----------------------------")
                print("Congratulations! You've Won!")
                print("----------------------------")
                print("----------------------------")      
                print()         
                break
    else:
        break       
    repeat_loop = input("Would You Like To Play Again? (Y/N): ")
    if repeat_loop == "N":
        game_running = False
        print()


