from processors.text_processor import text_processor
from processors.vector_processor import vector_processor

F_q = [0,1] # TODO: patikrint kūno taisyklingumą
q = len(F_q)
p_e = 0.01

vector = [0,0,1,0,0,1,0,0,1,0,0,1]

if len(vector) != 12:
    print(f'vector length is {len(vector)}. Should be 12')
    exit()

# text_processor(F_q, q, p_e)
# exit()

vector_processor(vector, p_e, F_q)
exit()



