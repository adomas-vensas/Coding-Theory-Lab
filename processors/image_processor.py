import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
from utilities import decimal_to_base


def image_processor(image_path:str, p_e:float, F_q:str) -> None:

    # img = mpimg.imread(image_path)
    # plt.imshow(img)
    # plt.axis('off')  # Turn off axes for a cleaner display
    # plt.show()

    img = Image.open(image_path)
    img = img.convert("RGB")
    pixels = list(img.getdata())
    
    result_pixels = []

    for (r, g, b) in pixels:
        encoded_r = decimal_to_base(r, len(F_q))
        encoded_g = decimal_to_base(g, len(F_q))
        encoded_b = decimal_to_base(b, len(F_q))
        

        result_pixels.append((encoded_r, encoded_g, encoded_b))




    print(pixels[210:300])

    pass