import random
math_quiz = [
    {"q": "What is 5 + 7?", "a": "12"},
    {"q": "What is 9 - 3?", "a": "6"},
    {"q": "What is 6 × 4?", "a": "24"},
    {"q": "What is 15 ÷ 3?", "a": "5"},
    {"q": "What is the square of 8?", "a": "64"}
]
gk_quiz = [
    {"q": "What is the capital of Japan?", "a": "Tokyo"},
    {"q": "How many continents are there?", "a": "7"},
    {"q": "Who painted the Mona Lisa?", "a": "Leonardo da Vinci"},
    {"q": "What is the largest ocean?", "a": "Pacific Ocean"},
    {"q": "Which planet is known as the Red Planet?", "a": "Mars"}
]
science_quiz = [
    {"q": "What gas do plants breathe in?", "a": "Carbon dioxide"},
    {"q": "What is H2O commonly known as?", "a": "Water"},
    {"q": "Which planet is closest to the Sun?", "a": "Mercury"},
    {"q": "How many bones are in an adult human body?", "a": "206"},
    {"q": "What force pulls objects toward Earth?", "a": "Gravity"}
]
english_quiz = [
    {"q": "What is the synonym of 'happy'?", "a": "Joyful"},
    {"q": "What is the antonym of 'fast'?", "a": "Slow"},
    {"q": "Correct spelling: 'recieve' or 'receive'?", "a": "receive"},
    {"q": "What is the plural of 'child'?", "a": "Children"},
    {"q": "Fill in the blank: 'He ___ going to school.'", "a": "is"}
]
capital_quiz = [
    {"q": "What is the capital of France?", "a": "Paris"},
    {"q": "What is the capital of Bangladesh?", "a": "Dhaka"},
    {"q": "What is the capital of Canada?", "a": "Ottawa"},
    {"q": "What is the capital of Australia?", "a": "Canberra"},
    {"q": "What is the capital of Italy?", "a": "Rome"}
]

score = 0

def randomizer():
    all_questions = math_quiz + gk_quiz + science_quiz + english_quiz + capital_quiz
    return random.sample(all_questions,5)


def select(a):
    score = 0
    val = []
    if a == 1:
        val = math_quiz
    elif a == 2:
        val = gk_quiz
    elif a == 3:
        val = science_quiz
    elif a == 4:
        val = english_quiz
    elif a == 5:
        val = capital_quiz
    elif a == 6:
        val = randomizer()

    for i in range(len(val)):
        question = val[i]["q"]
        ans = val[i]["a"]
        if input(question+ " ").strip().upper() == ans.upper():
            print("correct\n")
            score += 1
        else:
            print(f"Wrong!!!!. Correct is {ans}\n")
    print(f"your score is {score}\n")


def main():
    while True:
        a = int(input("Welcome to the short quiz app. Pick any topic\n" \
        "1. Math\n" \
        "2. General Knowledge\n" \
        "3. Science\n" \
        "4. English\n" \
        "5. Country Capital\n" \
        "6. Let me decide\n" \
        "7. Stop\n"))

        if a == 7: 
            break
        else:
            select(a)

main()