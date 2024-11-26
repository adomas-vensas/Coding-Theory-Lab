from utilities import text_to_vectors, base_to_decimal
from decoder import decode
from channel import send
from encoder import encode

def text_processor(text:str, F_q:list, p_e:float) -> None:
    text_vectors = text_to_vectors(text, F_q)

    result_1, result_2 = "", ""
    for i in text_vectors:
        result_1 += scenario_1(i, p_e, F_q)
        result_2 += scenario_2(i, p_e, F_q)


    print("Original:")
    print(text)
    
    print()
    print('Scenario 1:')
    print(result_1)

    print()
    print('Scenario 2:')
    print(result_2)

    
def scenario_1(regular_vector:list, p_e:float, F_q:list):
    received_vector, _ = send(regular_vector, p_e, F_q)
    decoded_c = get_char(received_vector, F_q)
    return decoded_c


def scenario_2(regular_vector:list, p_e:float, F_q:list):
    encoded_vector = encode(regular_vector, F_q)
    received_vector, _ = send(encoded_vector, p_e, F_q)
    decoded_vector, msg = decode(received_vector, F_q)

    if msg is not None:
        print(msg)
        exit()
    
    decoded_c = get_char(decoded_vector, F_q)
    return decoded_c


def get_char(vector:list, F_q:list):
    decimal_c = base_to_decimal(vector, len(F_q))

    if 0 <= decimal_c <= 128:
        return chr(decimal_c)
    
    return chr(decimal_c % 128)

