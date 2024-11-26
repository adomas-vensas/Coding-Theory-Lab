from processors.text_processor import text_processor
from processors.vector_processor import vector_processor
from processors.image_processor import image_processor
import re
import keyboard


F_q:list = [0,1]

def main():

    print("Golay code implementation for Coding Theory Lab")
    print()
    
    p_e = enter_probability()

    print("Select an option:")
    print("1. Process binary vector")
    print("2. Process text")
    print("3. Process an image")

    print("If you wish to quit, press CTRL+C")

    selection = enter_selection()

    if selection == 1:
        vector_selection(p_e)
    elif selection == 2:
        text_selection(p_e)
    elif selection == 3:
        image_selection(p_e)


def enter_selection() -> int:
    choice = input("Enter only the option number and pres ENTER: ")
    regex = r"^[123]$"

    while not re.match(regex, choice):
        print("Incorrect input!")
        choice = input("Enter only the option number and pres ENTER: ")

    print()

    return int(choice)


def enter_probability() -> float:
    number = input("Select an Error probability - a number in the interval [0, 1]: ")

    while True:
        try:
            p_e:float = float(number)

            if not 0 <= p_e <= 1:
                print("Incorrect input")
                number = input("Select an Error probability - a number in the interval [0, 1]: ")
                continue
            
            return p_e
        except:
            print("Not a number")
            number = input("Select an Error probability - a number in the interval [0,1]: ")
            continue
    

def vector_selection(p_e:float) -> None:
    print("Enter a 12 digit vector consisting only of {0, 1} and press ENTER:")
    user_input = input()

    regex = r"^[01]{12}$"
    while not re.match(regex, user_input):
        print("Incorrect input!")
        print("Enter a 12 digit vector consisting only of {0, 1} and press ENTER:")
        user_input = input()
    
    print()

    vector = [int(i) for i in user_input]
    vector_processor(vector, p_e, F_q)


def text_selection(p_e:float) -> None:
    print("Enter any text in the ENGLISH letters, arabic numbers and punctuation marks and press SHIFT+ENTER:")
    
    user_input = ''
    regex = r'^[A-Za-z0-9\n .,!?\'"-()]+$'

    while True:
        line = input()
        if keyboard.is_pressed("shift+enter"):
            break
        
        if not re.match(regex, line):
            print("Incorrect input! Only ENGLISH letters, arabic numbers and punctuation marks!")
            continue

        user_input += '\n' + line
    
    if len(user_input) == 0:
        print("Text cannot be empty")
        exit()

    text_processor(user_input, F_q, p_e)


def image_selection(p_e:float) -> None:
    # image_path = './processors/owl.png'
    # image_processor(image_path, p_e, F_q)
    pass