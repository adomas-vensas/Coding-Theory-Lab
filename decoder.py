from matrices import H, B
from utilities import multiply_vector_with_matrix


def decode(received_vector:list, F_q:list) -> tuple[list, str]:
    w = add_control_coordinate(received_vector)
    
    s = multiply_vector_with_matrix(w, H, F_q)
    u = calculate_u(True, s, F_q)

    if u != []:
        return generate_result(w, u, F_q), None

    sB = multiply_vector_with_matrix(s, B, F_q)
    u = calculate_u(False, sB, F_q)

    if u != []:
        return generate_result(w, u, F_q), None

    return [], '[ERROR] Could not decode message. Requesting retransmission.'


def generate_result(w:list, u:list, F_q:list) -> list:
    if len(w) != len(u):
        raise ValueError("List are not equal length")

    c = [0] * len(u)

    for i in range(len(u)):
        c[i] = (w[i] + u[i]) % len(F_q)
    c.pop()

    return c[:12]


def calculate_u(isFirst:bool, s: list, F_q:list) -> list:
    if count_weight(s) <= 3:
        return s + [0] * 12 if isFirst else [0] * 12 + s

    for i in range(len(B)):
        temp_vector = [0] * len(s)
        for j in range(len(s)):
            temp_vector[j] = (s[j] + B[i][j]) % len(F_q)

        if count_weight(temp_vector) <= 2:
            e_i = [0 for _ in range(12)]
            e_i[i] = 1
            return temp_vector + e_i if isFirst else e_i + temp_vector

    return []


def add_control_coordinate(received_vector:list) -> list:
    w = received_vector.copy()
    weight = count_weight(w)

    if weight % 2 != 0:
        w.append(0)
    else:
        w.append(1)
    
    return w


def count_weight(vector):
    weight = 0
    
    for i in vector:
        if i != 0:
            weight += 1
    
    return weight