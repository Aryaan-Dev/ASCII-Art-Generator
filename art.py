# import ascii_magic
# print(dir(ascii_magic))
# # Print the version of ascii_magic
# print(f"ASCII Magic version: {ascii_magic.__version__ if hasattr(ascii_magic, '__version__') else 'unknown'}")


# import ascii_magic
# import inspect
# # Print the function signature
# print(inspect.signature(ascii_magic.from_image))

import ascii_magic
from PIL import Image

img = ascii_magic.from_image("cod.png")
img.to_terminal(columns=100, char="#")