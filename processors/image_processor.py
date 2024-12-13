import matplotlib.pyplot as plt
from PIL import Image
from utilities import pixels_to_vectors, base_to_decimal
from channel import send
from encoder import encode
from decoder import decode


def image_processor(image_path:str, p_e:float, F_q:str) -> None:
    """
    Processes image input
    """
    
    #Prepare image for processing
    img = Image.open(image_path)
    img = img.convert("RGB")
    pixels = list(img.getdata()) #Extract image colors - tuples (R, G, B)
    
    converted_pixels = pixels_to_vectors(pixels, F_q)
    result_1, result_2 = [], []

    for converted_color in converted_pixels:
        color_1 = scenario_1(converted_color, p_e, F_q)
        color_2 = scenario_2(converted_color, p_e, F_q)


        result_1.append(color_1)
        result_2.append(color_2)

    _, axs = plt.subplots(1, 3, figsize=(15, 5))

    show_image(pixels, img.size, axs[0], title='Original Image')
    show_image(result_1, img.size, axs[1], title='Scenario 1')
    show_image(result_2, img.size, axs[2], title='Scenario 2')

    plt.tight_layout()
    plt.show()


def show_image(pixels, image_size: tuple[int, int], ax, title: str) -> None:
    """
    Shows the result image
    """
    
    img = Image.new('RGB', image_size)
    img.putdata(pixels)

    ax.imshow(img)
    ax.axis('off')
    ax.set_title(title)


def scenario_1(converted_color, p_e:float, F_q:list) -> tuple[int, int, int]:
    """
    Executing the first exercise scenario (no encoding)
    Returns: color list
    """

    (r, g, b) = converted_color

    decimal_r = process_color_1(r, p_e, F_q)
    decimal_g = process_color_1(g, p_e, F_q)
    decimal_b = process_color_1(b, p_e, F_q)

    return (decimal_r, decimal_g, decimal_b)


def process_color_1(rgb:list, p_e:float, F_q:list) -> int:
    """
    Sends and converts individual color values and converts to decimal base
    Returns: Individual color value
    """
    
    received_rgb, _ = send(rgb, p_e, F_q)
    decimal_rgb = base_to_decimal(received_rgb, len(F_q))
    return decimal_rgb


def scenario_2(converted_color, p_e:float, F_q:list) -> tuple[int, int, int]:
    """
    Executing the second exercise scenario (with encoding)
    Returns: color list
    """
    
    (r, g, b) = converted_color

    decimal_r = process_color_2(r, p_e, F_q)
    decimal_g = process_color_2(g, p_e, F_q)
    decimal_b = process_color_2(b, p_e, F_q)

    return (decimal_r, decimal_g, decimal_b)


def process_color_2(converted_rgb:list, p_e:float, F_q:list) -> int:
    """
    Encodes, sends, decodes and converts individual color values and converts to decimal base 
    Returns: Individual color value
    """

    # Counting how many zeros are still needed to reach 12 digits
    zero_amount = 12 - len(converted_rgb)
    converted_rgb = [0] * zero_amount + converted_rgb

    encoded_rgb = encode(converted_rgb, F_q)
    received_rgb, _ = send(encoded_rgb, p_e, F_q)

    # Reseting the zeros that might have been randomized
    received_rgb = [0] * zero_amount + received_rgb[zero_amount:]
    decoded_rgb, msg1 = decode(received_rgb, F_q)

    if msg1 is not None:
        print(msg1)
        exit()
    
    decimal_rgb = base_to_decimal(decoded_rgb, len(F_q))
    return decimal_rgb