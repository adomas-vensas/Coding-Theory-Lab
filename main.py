from processors.text_processor import text_processor
from processors.vector_processor import vector_processor
from processors.image_processor import image_processor

F_q = [0,1]
p_e = 0.01


# text_processor(F_q, p_e)
# exit()

vector = [0,0,1,0,0,1,0,0,1,0,0,1]

if len(vector) != 12:
    print(f'vector length is {len(vector)}. Should be 12')
    exit()

# vector_processor(vector, p_e, F_q)
# exit()

image_path = './processors/owl.png'
image_processor(image_path, p_e, F_q)



