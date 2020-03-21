from API import Encoder

encoder = Encoder()

# English only support
text = 'hello'

text = (encoder.coding(text))  # ->  |-|.☰.|_.|_..☢.

text = (encoder.encoding(text))  # ->  HELLO
