import random
import time
import os

# Logic gate functions return scrambled truth table and correct answer
def and_gate():
    table = [
        "0, 0 = 0",
        "1, 0 = 0",
        "0, 1 = 0",
        "1, 1 = 1"
    ]
    return scramble_table(table), 'and'

def or_gate():
    table = [
        "0, 0 = 0",
        "1, 0 = 1",
        "0, 1 = 1",
        "1, 1 = 1"
    ]
    return scramble_table(table), 'or'

def not_gate():
    table = [
        "0 = 1",
        "1 = 0"
    ]
    return scramble_table(table), 'not'

def buffer():
    table = [
        "1 = 1",
        "0 = 0"
    ]
    return scramble_table(table), 'buffer'

def nor_gate():
    table = [
        "0, 0 = 1",
        "1, 0 = 0",
        "0, 1 = 0",
        "1, 1 = 0"
    ]
    return scramble_table(table), 'nor'

def nand_gate():
    table = [
        "0, 0 = 1",
        "1, 0 = 1",
        "0, 1 = 1",
        "1, 1 = 0"
    ]
    return scramble_table(table), 'nand'

def xor_gate():
    table = [
        "0, 0 = 0",
        "1, 0 = 1",
        "0, 1 = 1",
        "1, 1 = 0"
    ]
    return scramble_table(table), 'xor'

def xnor_gate():
    table = [
        "0, 0 = 1",
        "1, 0 = 0",
        "0, 1 = 0",
        "1, 1 = 1"
    ]
    return scramble_table(table), 'xnor'

# Scrambles the order of the truth table rows
def scramble_table(table):
    random.shuffle(table)  # Shuffle the list in place
    return '\n'.join(table)  # Convert back to string format

# Store function references
funcs = [and_gate, or_gate, buffer, not_gate, nor_gate,nand_gate, xor_gate, xnor_gate]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clears console for a fresh question

def start_quiz():
    total_questions = 10
    points = 0
    wrong = []

    input("Press Enter when you are ready to start the quiz...")  # Start only when ready
    start_time = time.time()  # Start the timer

    for i in range(total_questions):
        clear_screen()

        print('''Write the corresponding logic gate name: 
        and, or, not, nor, nand, xor, xnor
        ''')

        print(f"Question {i + 1}/{total_questions}")  # Show question number
        rand_gate, correct_answer = random.choice(funcs)()  # Get a random gate question
        print(rand_gate)  # Print shuffled truth table

        your_ans = input('Answer: ').strip().lower()  # Normalize input

        if your_ans == correct_answer:
            print('Correct!')
            points += 1
        else:
            print(f'Incorrect! The correct answer was: {correct_answer}')
            wrong.append(f'{correct_answer}')
        time.sleep(1)  # Short pause before next question

    total_time = round(time.time() - start_time, 2)  # Total time taken in seconds
    print(f"\nTHAT'S THE END OF YOUR QUIZ!\nYou got {int(points/total_questions*100)}%\n{total_time} seconds.\n")
    time.sleep(1)
    if wrong:
        print('The following tables you got wrong:')
        for i, wrong_table in enumerate(wrong, start= 1):
            print (f'{i}. {wrong_table.title()} table')

# Run the quiz
start_quiz()

# display the truth table and the answer for the logic gate that you did not get correct
