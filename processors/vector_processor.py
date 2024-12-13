from decoder import decode
from channel import send
from encoder import encode

import re
import keyboard
import tkinter as tk
from tkinter import simpledialog, messagebox

def vector_processor(vector:list, p_e:float, F_q:list) -> None:
    """
    Processes vector input
    """
    
    encoded_vector = encode(vector, F_q)

    print(f'Encoded vector:  {encoded_vector}')

    received_vector, error_pos = send(encoded_vector, p_e, F_q)

    print(f'Received vector: {received_vector}')
    print(f'Error count: {len(error_pos)}')
    print(f'Error pos: {error_pos}')

    edited_vector = edit_received_vector(encoded_vector, received_vector)
    print(f'Edited vector:   {edited_vector}')

    decoded_vector, message = decode(edited_vector, F_q)

    if message is not None:
        print(message)
        exit()
    print(f'Given vector:    {vector}')
    print(f'Decoded vector:  {decoded_vector}')

    print("Press ESC to quit...")
    keyboard.wait('esc')


def edit_received_vector(original_vector:list, vector:list) -> list:
    """
    Opens a dialog to edit the received from channel vector
    Returns: the edited vector
    """
    
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)

    str_original = "".join(map(str, original_vector))  # Convert to strings
    str_vector = "".join(map(str, vector))

    updated_vector = None

    while True:
        updated_vector = simpledialog.askstring(
            "Edit Vector", 
            f"Encoded vector:\n{str_original}\n"
            f"Received encoded vector:\n{str_vector}\n"
            f"Correct the received vector (only 0 and 1 allowed):",
            initialvalue=str_vector
        )

        if updated_vector is None:  # User canceled
            root.destroy()
            return original_vector

        if re.match(r'^[01]{23}$', updated_vector):
            break

        messagebox.showerror("Invalid Input", "Only a vector of length 23 consisting of {0, 1} is correct. Please try again.")

    root.destroy()

    return [int(i) for i in updated_vector]