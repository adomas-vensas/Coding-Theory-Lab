from utilities import multiply_vector_with_matrix
from matrices import G

def encode(vector:list, F_q:list) -> list:
    """
    Encodes a vector
    Returns: encoded vector
    """
    
    encoded_vector = multiply_vector_with_matrix(vector, G, F_q)
    return encoded_vector
