import random


def send(encoded_vector:list, p_e:float, F_q:list) -> tuple[list, list]:
    received_vector = []
    error_pos = []

    for i in encoded_vector:
        a = random.random()

        if a > p_e:
            received_vector.append(i)
        else:
            temp = [x for x in F_q if x != i] # Remove 'i' from F_q
            received_vector.append(random.choice(temp))

            error_pos.append(len(received_vector) - 1)

    return received_vector, error_pos


