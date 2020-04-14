# ~-~ Author: Ythosa ~-~ #

from API import Encoder

# English only support

# Usign Example
text = 'hello'

text = Encoder.coding(text)  # ->  |-|.☰.|_.|_..☢.

text = Encoder.encoding(text) # ->  hello

# OR
text = input()
text = Encoder.coding(text)
print(text)

text = Encoder.encoding(text)
print(text)

# print(help(Encoder.encoding))
# print(help(Encoder.coding))
