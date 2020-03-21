import itertools
from collections import namedtuple


class Encoder:
    def __init__(self):
        couple = namedtuple('couple', ['code', 'encode'])
        self.__alphabet = (
            couple(code='A', encode='.@.'),
            couple(code='B', encode='.8.'),
            couple(code='С', encode='.⊂.'),
            couple(code='D', encode='.⊃.'),
            couple(code='E', encode='.☰.'),
            couple(code='F', encode='.≔.'),
            couple(code='G', encode='⅁..'),
            couple(code='H', encode='|-|'),
            couple(code='I', encode='|..'),
            couple(code='J', encode='⌡..'),
            couple(code='K', encode='|<.'),
            couple(code='L', encode='|_.'),
            couple(code='M', encode='|⋎|'),
            couple(code='N', encode='.ℵ.'),
            couple(code='O', encode='.☢.'),
            couple(code='P', encode='.|^'),
            couple(code='Q', encode='.☢ᵕ'),
            couple(code='R', encode='.≳.'),
            couple(code='S', encode='.⌇.'),
            couple(code='T', encode='.✝.'),
            couple(code='U', encode='.⊍.'),
            couple(code='V', encode='\./'),
            couple(code='W', encode='|v|'),
            couple(code='X', encode='.✕.'),
            couple(code='Y', encode='.⋎.'),
            couple(code='Z', encode='‾/_'),
        )

    def coding(self, text: str):
        text = list(itertools.chain(text.upper()))
        coded_text = []
        for letter in text:
            completed = False
            for coding in self.__alphabet:
                if coding.code == letter:
                    completed = True
                    coded_text.append(coding.encode)
                if completed:
                    break
            if not completed:
                coded_text.append(letter)
        coded_string = "".join(coded_text)
        return coded_string

    def encoding(self, text):
        text = [text[i:i + 3] for i in range(0, len(text), 3)]
        encoded_text = []
        for letter in text:
            completed = False
            for coding in self.__alphabet:
                if coding.encode == letter:
                    completed = True
                    encoded_text.append(coding.code)
                if completed:
                    break
            if not completed:
                encoded_text.append(letter)
        encoded_string = "".join(encoded_text)
        return encoded_string
