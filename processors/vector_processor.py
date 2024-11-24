from decoder import decode
from channel import send
from encoder import encode

def vector_processor(vector:list, p_e:float, F_q:list) -> None:
    encoded_vector = encode(vector, F_q)

    print(f'Encoded vector:  {encoded_vector}')

    received_vector, error_pos = send(encoded_vector, p_e, F_q)

    print(f'Received vector: {received_vector}')
    print(f'Error count: {len(error_pos)}')
    print(f'Error pos: {error_pos}')

    decoded_vector, message = decode(received_vector, F_q)

    if message is not None:
        print(message)
        exit()

    print(f'Given vector:   {vector}')
    print(f'Decoded vector: {decoded_vector}')