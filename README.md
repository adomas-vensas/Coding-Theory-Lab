The user of the program should have the ability to specify a specific field (i.e., q, except in cases where qq can only take a single value, such as q=2), a specific code (i.e., the parameters listed in the column "Code Parameters"), and the error probability pepe​.

From the user's perspective, the program should implement three scenarios:
- The user enters a vector of a specified length composed of elements from the field Fq​.
        The program checks whether the vector length is valid (exception: if a convolutional code is used, the message length can be arbitrary, and the program should not enforce or validate the length in this case).
        The program encodes the vector using the code C, displays the encoded vector, sends it through a channel, displays the vector received from the channel, reports how many errors occurred and their positions, decodes the received vector, and displays the result.
        The user should have the ability to edit the vector received from the channel before decoding it to specify errors where and how many they need.
- The user enters text (the text can consist of multiple lines).
        The program splits the given text into vectors of the required length composed of elements from the field Fq (if a convolutional code is used, it does not split the text).
            Each vector is sent through the channel without using a code; the program reconstructs the text from the received vectors and displays it.
            Each vector is encoded, sent through the channel, and decoded; the program reconstructs the text from the received vectors and displays it.
- The user specifies an image (in BMP format, as it best visualizes channel distortions).
        The program opens and displays the image.
        It splits the given image into vectors of the required length composed of elements from the field Fq​ (if a convolutional code is used, it does not split the image).
            Each vector is sent through the channel without using a code; the program reconstructs the image from the received vectors and displays it.
            Each vector is encoded, sent through the channel, and decoded; the program reconstructs the image from the received vectors and displays it.
